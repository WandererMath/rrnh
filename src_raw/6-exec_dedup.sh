#!/bin/bash
#SBATCH --job-name=6-dedup
#SBATCH --output=2-exec_trim-output.txt
#SBATCH --time=04:00:00
#SBATCH --account=PAS0182  # Specify PI's account here
#SBATCH --ntasks=4                   # Number of parallel tasks (processes)
#SBATCH --cpus-per-task=12            # CPUs allocated per task (adjust as needed)
#SBATCH --constraint=48core



# Your job's commands go here
source ~/.bashrc
conda activate env1
fastp -i ./data/merged_assembled/A03-trim-merged.assembled.fastq -o ./data/dedup/A03-trim-merged-dedup.fastq --dedup -Q -A -G -j /dev/null -h /dev/null --thread 12 --trim_poly_x --length_required 20 & 
fastp -i ./data/merged_assembled/C03-trim-merged.assembled.fastq -o ./data/dedup/C03-trim-merged-dedup.fastq --dedup -Q -A -G -j /dev/null -h /dev/null --thread 12 --trim_poly_x --length_required 20 & 
fastp -i ./data/merged_assembled/B02-trim-merged.assembled.fastq -o ./data/dedup/B02-trim-merged-dedup.fastq --dedup -Q -A -G -j /dev/null -h /dev/null --thread 12 --trim_poly_x --length_required 20 & 
fastp -i ./data/merged_assembled/A01-trim-merged.assembled.fastq -o ./data/dedup/A01-trim-merged-dedup.fastq --dedup -Q -A -G -j /dev/null -h /dev/null --thread 12 --trim_poly_x --length_required 20 & 
fastp -i ./data/merged_assembled/C01-trim-merged.assembled.fastq -o ./data/dedup/C01-trim-merged-dedup.fastq --dedup -Q -A -G -j /dev/null -h /dev/null --thread 12 --trim_poly_x --length_required 20 & 
fastp -i ./data/merged_assembled/B01-trim-merged.assembled.fastq -o ./data/dedup/B01-trim-merged-dedup.fastq --dedup -Q -A -G -j /dev/null -h /dev/null --thread 12 --trim_poly_x --length_required 20 & 
fastp -i ./data/merged_assembled/B03-trim-merged.assembled.fastq -o ./data/dedup/B03-trim-merged-dedup.fastq --dedup -Q -A -G -j /dev/null -h /dev/null --thread 12 --trim_poly_x --length_required 20 & 
fastp -i ./data/merged_assembled/C02-trim-merged.assembled.fastq -o ./data/dedup/C02-trim-merged-dedup.fastq --dedup -Q -A -G -j /dev/null -h /dev/null --thread 12 --trim_poly_x --length_required 20 & 
fastp -i ./data/merged_assembled/A02-trim-merged.assembled.fastq -o ./data/dedup/A02-trim-merged-dedup.fastq --dedup -Q -A -G -j /dev/null -h /dev/null --thread 12 --trim_poly_x --length_required 20 & 
wait