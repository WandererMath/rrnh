import os


# Source init.sh first

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


raw_fastq_dir="./raw/"
trim_fastq_dir = "./data/trim/"


sampleid_fastq_dict = find_sample_fastqs(raw_fastq_dir)

'''
for a in sampleid_fastq_dict:
    print(a)
    print(sampleid_fastq_dict[a])'''

def trim():
    with open("2-trim-cmds.txt", 'w') as f:
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
            f.write(command+" &\n")

if __name__=="__main__":
    trim()