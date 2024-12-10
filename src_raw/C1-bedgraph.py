import os


def longest_common_substring(s1, s2):
    """
    Finds the length of the longest common substring between two strings.
    """
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    longest = 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                longest = max(longest, matrix[i][j])
    
    return longest

def find_best_match(target, candidates):
    """
    Finds the string in the list that has the most matches with the target string.
    """
    best_match = None
    max_match_length = 0

    for candidate in candidates:
        match_length = longest_common_substring(target, candidate)
        if match_length > max_match_length:
            max_match_length = match_length
            best_match = candidate

    return best_match

# Example usage
target_string = "hello"
candidate_list = ["hallo", "world", "hell", "hero", "help"]

best_match = find_best_match(target_string, candidate_list)
print(f"The best match for '{target_string}' is '{best_match}'.")





def get_files(folder_path, end):
    txt_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(end):
                txt_files.append(os.path.join(root, file))
    return txt_files


def get_files_base(folder_path, end):
    txt_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(end):
                txt_files.append(file)
    return txt_files


# PATH_SAM := output_loc
def bedgraph(output_loc, PATH_OUT, dedup_out_loc , PATH_NORM_OUT):
    ## compute genome coverage by midpoint of RNASeq read
    # compute genome coverage by endpoint-14  of RNASeq read
    genome_coverage_counts = {}
    with open(output_loc, "r") as f:
        for row in f:
            try:
                row = row.replace("\n","").split("\t")
                subj = row[2]

                direction_flag = row[1]

                # ######
                if direction_flag=="16":
                    #print(direction)
                    direction='-'
                else:
                    direction='+'

                subj_start = int(row[3])
                align_seq = row[4]
                align_seq = row[9]

                len_align = len(align_seq)

                #position_on_genome_to_add_count = subj_start + int(len_align / 2) - 1
                position_on_genome_to_add_count = subj_start + len_align - 14
                if subj not in genome_coverage_counts:
                    genome_coverage_counts[subj] = {}
                if direction not in genome_coverage_counts[subj]:
                    genome_coverage_counts[subj][direction] = {}
                if position_on_genome_to_add_count not in genome_coverage_counts[subj][direction]:
                    genome_coverage_counts[subj][direction][position_on_genome_to_add_count] = 0
                genome_coverage_counts[subj][direction][position_on_genome_to_add_count] += 1
            except:
                pass
    f.close()

    #print(genome_coverage_counts)
    # Split writing output by plus and negative strand!
    # Create bedgraph output file to visualize genome coverage with IGV Browser
    with open(PATH_OUT+ "-plus-cov.bedgraph", "w") as f:
        f.write("track type=bedGraph\n")
        for subj in genome_coverage_counts:
            if '+' not in genome_coverage_counts[subj]:
                continue
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

    with open(PATH_OUT + "-minus-cov.bedgraph", "w") as f:
        f.write("track type=bedGraph\n")
        for subj in genome_coverage_counts:
            if '-' not in genome_coverage_counts[subj]:
                continue
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
    with open(PATH_NORM_OUT + "-plus.bedgraph", "w") as f:
        f.write("track type=bedGraph\n")
        for subj in genome_coverage_counts:
            if '+' not in genome_coverage_counts[subj]:
                continue
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

    with open(PATH_NORM_OUT + "-minus.bedgraph", "w") as f:
        f.write("track type=bedGraph\n")
        for subj in genome_coverage_counts:
            if '-' not in genome_coverage_counts[subj]:
                continue
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


DIR_SAM='../data/bowtie'
DIR_DEDUP='../data/dedup'
DIR_OUT='../data/genome_cov'
DIR_NORM_OUT='../data/norm_genome_cov'

os.makedirs(DIR_OUT, exist_ok=True)
os.makedirs(DIR_NORM_OUT, exist_ok=True)

sam_files=get_files_base(DIR_SAM, '.txt')
dedup_files=get_files(DIR_DEDUP, '.fastq')

print(sam_files)
print(dedup_files)
for file in sam_files:
    path_sam=os.path.join(DIR_SAM, file)
    path_out=os.path.join(DIR_OUT, file)
    path_norm_out=os.path.join(DIR_NORM_OUT, file)
    dedup_file=find_best_match(file, dedup_files)
    print(path_out, path_norm_out)
    bedgraph(path_sam, path_out, dedup_file, path_norm_out)
