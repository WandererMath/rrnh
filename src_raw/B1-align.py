#from B_init import *
import os, sys

SLURM='''#!/bin/bash
#SBATCH --job-name={}
#SBATCH --output={}
#SBATCH --time=04:00:00
#SBATCH --account=PAS0182  # Specify PI's account here
#SBATCH --ntasks=4                   # Number of parallel tasks (processes)
#SBATCH --cpus-per-task=12            # CPUs allocated per task (adjust as needed)
#SBATCH --constraint=48core

conda activate env1
'''.format(sys.argv[0].split(".")[0],sys.argv[0].split(".")[0]+".out")


def get_files(folder_path):
    txt_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".fastq"):
                txt_files.append(os.path.join(root, file))
    return txt_files

def basenames(files):
    return [file.split("/")[-1] for file in files]

INPUT=get_files("../data/merged_assembled")
INPUT_BASE=basenames(INPUT)
OUT_PATH="../data08B/bowtie"
os.makedirs(OUT_PATH, exist_ok=True)
ref_genome_loc ="../ref/Ecoli_BW25113"
print(INPUT)
print(INPUT_BASE)
def align():
    with open("B1.sh", 'w') as f:
        f.write(SLURM)
        for file, out in zip(INPUT, INPUT_BASE):

            #bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 ./data/dedup/A03-trim-merged-dedup.fastq >  ./data/bowtie/A03-bowtie2.txt 

            command="bowtie -q -3 5 -S {} {} > {}".format(ref_genome_loc,file,os.path.join(OUT_PATH, out+".txt"))
            f.write(command+" & \n")
        f.write("wait\n")

align()
