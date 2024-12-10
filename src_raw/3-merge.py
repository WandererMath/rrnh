from init_clean import *


def merge():
    with open("3-merge-cmds.txt", 'w') as f:
        for base_id in sampleid_fastq_dict:
            print("analyzing sample id:", base_id)
            R1, R2 = sampleid_fastq_dict[base_id]

            # run cutadapt for quality + adapter trimming
            # Running PHRED 20 from 5' and 3' ends
            trim_R1, trim_R2 = \
                trim_fastq_dir + base_id + "-trim_R1.fastq", \
                trim_fastq_dir + base_id + "-trim_R2.fastq"
            # run pear for read assembly
            # conda install -c bioconda pear
            merged_output = merged_all_dir + base_id + "-trim-merged"
            command = "pear" + \
                        " -f " + trim_R1 + \
                        " -r " + trim_R2 + \
                        " -o " + merged_output + \
                        " -n 20 --threads 12 --memory 4G"
            f.write(command+" & \n")
        f.write("wait\n")

merge()
