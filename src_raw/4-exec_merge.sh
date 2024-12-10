#!/bin/bash
#SBATCH --job-name=4-merge
#SBATCH --output=2-exec_trim-output.txt
#SBATCH --time=04:00:00
#SBATCH --account=PAS0182  # Specify PI's account here
#SBATCH --ntasks=4                   # Number of parallel tasks (processes)
#SBATCH --cpus-per-task=12            # CPUs allocated per task (adjust as needed)
#SBATCH --constraint=48core



# Your job's commands go here
source ~/.bashrc
conda activate env1
pear -f ./data/trim/A03-trim_R1.fastq -r ./data/trim/A03-trim_R2.fastq -o ./data/merged/A03-trim-merged -n 20 --threads 12 --memory 4G & 
pear -f ./data/trim/C03-trim_R1.fastq -r ./data/trim/C03-trim_R2.fastq -o ./data/merged/C03-trim-merged -n 20 --threads 12 --memory 4G & 
pear -f ./data/trim/B02-trim_R1.fastq -r ./data/trim/B02-trim_R2.fastq -o ./data/merged/B02-trim-merged -n 20 --threads 12 --memory 4G & 
pear -f ./data/trim/A01-trim_R1.fastq -r ./data/trim/A01-trim_R2.fastq -o ./data/merged/A01-trim-merged -n 20 --threads 12 --memory 4G & 
pear -f ./data/trim/C01-trim_R1.fastq -r ./data/trim/C01-trim_R2.fastq -o ./data/merged/C01-trim-merged -n 20 --threads 12 --memory 4G & 
pear -f ./data/trim/B01-trim_R1.fastq -r ./data/trim/B01-trim_R2.fastq -o ./data/merged/B01-trim-merged -n 20 --threads 12 --memory 4G & 
pear -f ./data/trim/B03-trim_R1.fastq -r ./data/trim/B03-trim_R2.fastq -o ./data/merged/B03-trim-merged -n 20 --threads 12 --memory 4G & 
pear -f ./data/trim/C02-trim_R1.fastq -r ./data/trim/C02-trim_R2.fastq -o ./data/merged/C02-trim-merged -n 20 --threads 12 --memory 4G & 
pear -f ./data/trim/A02-trim_R1.fastq -r ./data/trim/A02-trim_R2.fastq -o ./data/merged/A02-trim-merged -n 20 --threads 12 --memory 4G & 
wait