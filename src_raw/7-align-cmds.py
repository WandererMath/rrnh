from init_clean import *


def align():
    with open("7-align-cmds.txt", 'w') as f:
        for base_id in sampleid_fastq_dict:
            print("analyzing sample id:", base_id)
            R1, R2 = sampleid_fastq_dict[base_id]


            # Run alignments against reference genome
            # Remove last 5 nts from each read pair prior to conducting alignment!
            ref_genome_loc = "ref_files_for_genome_viewer/Ecoli_BW25113"
            output_loc = alignment_output_dir + base_id + "-bowtie1.txt"
            #print(base_id)
            sample_id = base_id
            dedup_out_loc = dedup_fastq_dir + sample_id + "-trim-merged-dedup.fastq"
            command = "bowtie" + \
                        " -q" + \
                        " -3 5" + \
                        " -x " + ref_genome_loc + \
                        " --best -S" + \
                        " " + dedup_out_loc + \
                        " " + output_loc
            #bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 ./data/dedup/A03-trim-merged-dedup.fastq >  ./data/bowtie/A03-bowtie2.txt 

            command="bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 {} > {}".format(dedup_out_loc,output_loc)
            f.write(command+" & \n")
        f.write("wait\n")

align()
