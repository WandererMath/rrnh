from init_clean import *


def dedup():
    with open("5-dedup-cmds.txt", 'w') as f:
        for base_id in sampleid_fastq_dict:
            print("analyzing sample id:", base_id)
            R1, R2 = sampleid_fastq_dict[base_id]

            # run cutadapt for quality + adapter trimming
            # Running PHRED 20 from 5' and 3' ends
            trim_R1, trim_R2 = \
                trim_fastq_dir + base_id + "-trim_R1.fastq", \
                trim_fastq_dir + base_id + "-trim_R2.fastq"
            
            merged_output = merged_all_dir + base_id + "-trim-merged"
            merged_output_loc = merged_fastq_dir + base_id + "-trim-merged" + ".assembled.fastq"
            # Dedup with Fastp
            # remove polyX 3' tails
            # re-do length filtering for short reads due to polyX tail trimming
            # Disable all other cleaning
            dedup_out_loc = dedup_fastq_dir + base_id + "-trim-merged-dedup.fastq"
            command = "fastp" + \
                        " -i " + merged_output_loc + \
                        " -o " + dedup_out_loc + \
                        " --dedup" + \
                        " -Q -A -G" + \
                        " -j /dev/null -h /dev/null" + \
                        " --thread 12" + \
                        " --trim_poly_x" + \
                        " --length_required 20"
            
            f.write(command+" & \n")
        f.write("wait\n")

dedup()
