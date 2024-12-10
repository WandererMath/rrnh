#!/bin/bash
#SBATCH --job-name=B1-align
#SBATCH --output=B1-align.out
#SBATCH --time=04:00:00
#SBATCH --account=PAS0182  # Specify PI's account here
#SBATCH --ntasks=4                   # Number of parallel tasks (processes)
#SBATCH --cpus-per-task=12            # CPUs allocated per task (adjust as needed)
#SBATCH --constraint=48core

conda activate env1
bowtie -q -3 5 -S ../ref/Ecoli_BW25113 ../data/merged_assembled/A01-trim-merged.assembled.fastq > ../data08B/bowtie/A01-trim-merged.assembled.fastq.txt & 
bowtie -q -3 5 -S ../ref/Ecoli_BW25113 ../data/merged_assembled/A02-trim-merged.assembled.fastq > ../data08B/bowtie/A02-trim-merged.assembled.fastq.txt & 
bowtie -q -3 5 -S ../ref/Ecoli_BW25113 ../data/merged_assembled/A03-trim-merged.assembled.fastq > ../data08B/bowtie/A03-trim-merged.assembled.fastq.txt & 
bowtie -q -3 5 -S ../ref/Ecoli_BW25113 ../data/merged_assembled/B01-trim-merged.assembled.fastq > ../data08B/bowtie/B01-trim-merged.assembled.fastq.txt & 
bowtie -q -3 5 -S ../ref/Ecoli_BW25113 ../data/merged_assembled/B02-trim-merged.assembled.fastq > ../data08B/bowtie/B02-trim-merged.assembled.fastq.txt & 
bowtie -q -3 5 -S ../ref/Ecoli_BW25113 ../data/merged_assembled/B03-trim-merged.assembled.fastq > ../data08B/bowtie/B03-trim-merged.assembled.fastq.txt & 
bowtie -q -3 5 -S ../ref/Ecoli_BW25113 ../data/merged_assembled/C01-trim-merged.assembled.fastq > ../data08B/bowtie/C01-trim-merged.assembled.fastq.txt & 
bowtie -q -3 5 -S ../ref/Ecoli_BW25113 ../data/merged_assembled/C02-trim-merged.assembled.fastq > ../data08B/bowtie/C02-trim-merged.assembled.fastq.txt & 
bowtie -q -3 5 -S ../ref/Ecoli_BW25113 ../data/merged_assembled/C03-trim-merged.assembled.fastq > ../data08B/bowtie/C03-trim-merged.assembled.fastq.txt & 
wait
