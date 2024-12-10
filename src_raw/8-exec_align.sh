#!/bin/bash
#SBATCH --job-name=8-align
#SBATCH --output=2-exec_trim-output.txt
#SBATCH --time=04:00:00
#SBATCH --account=PAS0182  # Specify PI's account here
#SBATCH --ntasks=4                   # Number of parallel tasks (processes)
#SBATCH --cpus-per-task=12            # CPUs allocated per task (adjust as needed)
#SBATCH --constraint=48core



# Your job's commands go here
source ~/.bashrc
conda activate env1
bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 ./data/dedup/A03-trim-merged-dedup.fastq > ./data/bowtie/A03-bowtie1.txt & 
bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 ./data/dedup/C03-trim-merged-dedup.fastq > ./data/bowtie/C03-bowtie1.txt & 
bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 ./data/dedup/B02-trim-merged-dedup.fastq > ./data/bowtie/B02-bowtie1.txt & 
bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 ./data/dedup/A01-trim-merged-dedup.fastq > ./data/bowtie/A01-bowtie1.txt & 
bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 ./data/dedup/C01-trim-merged-dedup.fastq > ./data/bowtie/C01-bowtie1.txt & 
bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 ./data/dedup/B01-trim-merged-dedup.fastq > ./data/bowtie/B01-bowtie1.txt & 
bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 ./data/dedup/B03-trim-merged-dedup.fastq > ./data/bowtie/B03-bowtie1.txt & 
bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 ./data/dedup/C02-trim-merged-dedup.fastq > ./data/bowtie/C02-bowtie1.txt & 
bowtie -q -3 5 -S ref_files_for_genome_viewer/Ecoli_BW25113 ./data/dedup/A02-trim-merged-dedup.fastq > ./data/bowtie/A02-bowtie1.txt & 
wait

