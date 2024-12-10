import os


def find_sample_fastqs(fastq_dir):
    """
    This function takes as input the directory location containing FASTQ files
    And outputs a python dictionary who's key is the base sample ID
    and value is a 2-item list, first item path to R1, second item path to R2

    Note: function assumes that paired end FASTQ files are named with _R1 and _R2
    """
    sampleid_fastq_dict = {}

    for filename in os.listdir(fastq_dir):
        if "_R1" in filename:
            base_id = filename.split("_R1")[0]
            index = 0
        elif "_R2" in filename:
            base_id = filename.split("_R2")[0]
            index = 1
        else:
            print("WARNING - Encountered unacceptable filetype for PE reads:", filename)

        if base_id not in sampleid_fastq_dict:
            sampleid_fastq_dict[base_id] = ["", ""]

        sampleid_fastq_dict[base_id][index] = fastq_dir + filename

    # check sampleid_fastq_dict for base_ids without 2 FASTQs
    for base_id in sampleid_fastq_dict:
        R1, R2 = sampleid_fastq_dict[base_id]

        if R1 == "" or R2 == "":
            raise Exception("Did not find both R1 and R2 for base_id:", base_id)

    return sampleid_fastq_dict


# Define paths to sequencing files at each step of cleaning
# Note: this is currently done explicitly, future todo script nicely
raw_fastq_dir = "../sequence_reads/KFredrick007/all-raw/"
trim_fastq_dir = "../sequence_reads/KFredrick007/trim/"
merged_fastq_dir = "../sequence_reads/KFredrick007/merged/"
merged_all_dir = "../sequence_reads/KFredrick007/merged_all/"
dedup_fastq_dir = "../sequence_reads/KFredrick007/dedup/"

# Define output directories of interest
alignment_output_dir = "bowtie_output_2/"
genome_coverage_out = "genome_cov/"
norm_genome_coverage_out = "norm_genome_cov/"

# Make directories. Future todo: wrap in function for space prettiness
os.makedirs(merged_fastq_dir, exist_ok=True)
os.makedirs(trim_fastq_dir, exist_ok=True)
os.makedirs(dedup_fastq_dir, exist_ok=True)
os.makedirs(alignment_output_dir, exist_ok=True)
os.makedirs(genome_coverage_out, exist_ok=True)
os.makedirs(merged_all_dir, exist_ok=True)
os.makedirs(norm_genome_coverage_out, exist_ok=True)

# find all FASTQs available in the directory
sampleid_fastq_dict = find_sample_fastqs(raw_fastq_dir)
for base_id in sampleid_fastq_dict:
    print("analyzing sample id:", base_id)
    R1, R2 = sampleid_fastq_dict[base_id]

    # run cutadapt for quality + adapter trimming
    # Running PHRED 20 from 5' and 3' ends
    trim_R1, trim_R2 = \
        trim_fastq_dir + base_id + "-trim_R1.fastq", \
        trim_fastq_dir + base_id + "-trim_R2.fastq"
    command = "cutadapt" + \
                " -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA" + \
                " -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT" + \
                " -o " + trim_R1 + \
                " -p " + trim_R2 + \
                " --discard-untrimmed" + \
                " --cores=12" + \
                " --pair-filter=any" + \
                " --minimum-length=20" + \
                " --maximum-length=55" + \
                " -q 20,20" + \
                " " + R1 + " " + R2
    os.system(command)

    # run pear for read assembly
    # conda install -c bioconda pear
    merged_output = merged_all_dir + base_id + "-trim-merged"
    command = "pear" + \
                " -f " + trim_R1 + \
                " -r " + trim_R2 + \
                " -o " + merged_output + \
                " -n 20 --threads 12 --memory 4G"
    os.system(command)

    # move the assembled file!
    merged_output_loc = merged_fastq_dir + base_id + "-trim-merged" + ".assembled.fastq"
    command = "mv " + merged_output + ".assembled.fastq" + " " + merged_output_loc
    os.system(command)
    
    # Dedup with Fastp
    # remove polyX 3' tails
    # re-do length filtering for short reads due to polyX tail trimming
    # Disable all other cleaning
    dedup_out_loc = dedup_fastq_dir + base_id + "-trim-merged-dedup.fastq"
    command = "./fastp" + \
                " -i " + merged_output_loc + \
                " -o " + dedup_out_loc + \
                " --dedup" + \
                " -Q -A -G" + \
                " -j /dev/null -h /dev/null" + \
                " --thread 12" + \
                " --trim_poly_x" + \
                " --length_required 20"
    os.system(command)

    # Run alignments against reference genome
    # Remove last 5 nts from each read pair prior to conducting alignment!
    ref_genome_loc = "/home/fung/Documents/sequence_activities/reference_genomes/EColi/Ecoli_BW25113"
    output_loc = alignment_output_dir + base_id + "-bowtie2.txt"
    sample_id = base_id.split("_")[1]
    dedup_out_loc = dedup_fastq_dir + "KFredrick007_" + sample_id + "-trim-merged-dedup.fastq"
    command = "bowtie" + \
                " -q" + \
                " -3 5" + \
                " -x " + ref_genome_loc + \
                " --best -S" + \
                " " + dedup_out_loc + \
                " " + output_loc
    os.system(command)

    # compute genome coverage by midpoint of RNASeq read
    genome_coverage_counts = {}
    with open(output_loc, "r") as f:
        for row in f:
            row = row.replace("\n","").split("\t")
            subj = row[2]

            direction = row[1]
            subj_start = int(row[3])
            align_seq = row[4]

            len_align = len(align_seq)

            position_on_genome_to_add_count = subj_start + int(len_align / 2) - 1
    
            if subj not in genome_coverage_counts:
                genome_coverage_counts[subj] = {}
            if direction not in genome_coverage_counts[subj]:
                genome_coverage_counts[subj][direction] = {}
            if position_on_genome_to_add_count not in genome_coverage_counts[subj][direction]:
                genome_coverage_counts[subj][direction][position_on_genome_to_add_count] = 0
            genome_coverage_counts[subj][direction][position_on_genome_to_add_count] += 1
    f.close()

    # Split writing output by plus and negative strand!
    # Create bedgraph output file to visualize genome coverage with IGV Browser
    with open(genome_coverage_out + base_id + "-plus-cov.bedgraph", "w") as f:
        f.write("track type=bedGraph\n")
        for subj in genome_coverage_counts:
            subject_covs = genome_coverage_counts[subj]["+"]

            position_coverages = []
            for position in subject_covs:
                count = subject_covs[position]
                position_coverages.append([int(position), int(count)])
            
            # sort 
            position_coverages = sorted(position_coverages, key = lambda x:x[0])

            for position, count in position_coverages:
                f.write(subj + "\t" + str(position) + "\t" + str(position + 1) + "\t" + str(count) + "\n")
    f.close()

    with open(genome_coverage_out + base_id + "-minus-cov.bedgraph", "w") as f:
        f.write("track type=bedGraph\n")
        for subj in genome_coverage_counts:
            subject_covs = genome_coverage_counts[subj]["-"]

            position_coverages = []
            for position in subject_covs:
                count = subject_covs[position]
                position_coverages.append([int(position), int(count)])
            
            # sort 
            position_coverages = sorted(position_coverages, key = lambda x:x[0])

            for position, count in position_coverages:
                f.write(subj + "\t" + str(position) + "\t" + str(position + 1) + "\t" + str(count) + "\n")
    f.close()

    # Write out a set of normalized genome coveage - counts per million normalization
    # get # of reads in the sample!
    counter = 0
    with open(dedup_out_loc, "r") as f:
        for row in f:
            counter += 1
    f.close()
    num_reads = counter / 4

    # Split writing output by plus and negative strand!
    with open(norm_genome_coverage_out + base_id + "-plus.bedgraph", "w") as f:
        f.write("track type=bedGraph\n")
        for subj in genome_coverage_counts:
            subject_covs = genome_coverage_counts[subj]["+"]

            position_coverages = []
            for position in subject_covs:
                count = subject_covs[position]

                norm_count = (10 ** 6) * count / num_reads

                position_coverages.append([int(position), float(norm_count)])
            
            # sort 
            position_coverages = sorted(position_coverages, key = lambda x:x[0])

            for position, count in position_coverages:
                f.write(subj + "\t" + str(position) + "\t" + str(position + 1) + "\t" + str(count) + "\n")
    f.close()

    with open(norm_genome_coverage_out + base_id + "-minus.bedgraph", "w") as f:
        f.write("track type=bedGraph\n")
        for subj in genome_coverage_counts:
            subject_covs = genome_coverage_counts[subj]["-"]

            position_coverages = []
            for position in subject_covs:
                count = subject_covs[position]

                norm_count = (10 ** 6) * count / num_reads

                position_coverages.append([int(position), float(norm_count)])
            
            # sort 
            position_coverages = sorted(position_coverages, key = lambda x:x[0])

            for position, count in position_coverages:
                f.write(subj + "\t" + str(position) + "\t" + str(position + 1) + "\t" + str(count) + "\n")
    f.close()

# run FastQC on raw reads
docker_root = "/home/fung/Documents/sequence_activities/Bioinformatic_Workflows/"
command = docker_root + "Nano-QualReport/run" + \
            " " + trim_fastq_dir + \
            " trim_fastqc/" + \
            " 12"
os.system(command)

# run FastQC on merged/trimmed reads
command = docker_root + "Nano-QualReport/run" + \
            " " + merged_fastq_dir + \
            " merged_trim_fastqc/" + \
            " 12"
os.system(command)

# run FastQC on deduplicated/merged/trimmed reads
command = docker_root + "Nano-QualReport/run" + \
            " " + dedup_fastq_dir + \
            " dedup_merged_trim_fastqc/" + \
            " 12"
os.system(command)

