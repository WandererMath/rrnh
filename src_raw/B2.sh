#!/bin/bash
#SBATCH --job-name=B2-align
#SBATCH --output=B2-align.out
#SBATCH --time=04:00:00
#SBATCH --account=PAS0182  # Specify PI's account here
#SBATCH --ntasks=4                   # Number of parallel tasks (processes)
#SBATCH --cpus-per-task=12            # CPUs allocated per task (adjust as needed)
#SBATCH --constraint=48core

conda activate env1
bowtie -q -3 5 -S -k 10 ../ref/Ecoli_BW25113 ../data07/dedup/KFredrick007_A01-trim-merged-dedup.fastq > ../data07/bowtie-d/KFredrick007_A01-trim-merged-dedup.fastq.txt & 
bowtie -q -3 5 -S -k 10 ../ref/Ecoli_BW25113 ../data07/dedup/KFredrick007_A02-trim-merged-dedup.fastq > ../data07/bowtie-d/KFredrick007_A02-trim-merged-dedup.fastq.txt & 
bowtie -q -3 5 -S -k 10 ../ref/Ecoli_BW25113 ../data07/dedup/KFredrick007_A03-trim-merged-dedup.fastq > ../data07/bowtie-d/KFredrick007_A03-trim-merged-dedup.fastq.txt & 
bowtie -q -3 5 -S -k 10 ../ref/Ecoli_BW25113 ../data07/dedup/KFredrick007_B01-trim-merged-dedup.fastq > ../data07/bowtie-d/KFredrick007_B01-trim-merged-dedup.fastq.txt & 
bowtie -q -3 5 -S -k 10 ../ref/Ecoli_BW25113 ../data07/dedup/KFredrick007_B02-trim-merged-dedup.fastq > ../data07/bowtie-d/KFredrick007_B02-trim-merged-dedup.fastq.txt & 
bowtie -q -3 5 -S -k 10 ../ref/Ecoli_BW25113 ../data07/dedup/KFredrick007_B03-trim-merged-dedup.fastq > ../data07/bowtie-d/KFredrick007_B03-trim-merged-dedup.fastq.txt & 
bowtie -q -3 5 -S -k 10 ../ref/Ecoli_BW25113 ../data07/dedup/KFredrick007_C01-trim-merged-dedup.fastq > ../data07/bowtie-d/KFredrick007_C01-trim-merged-dedup.fastq.txt & 
bowtie -q -3 5 -S -k 10 ../ref/Ecoli_BW25113 ../data07/dedup/KFredrick007_C02-trim-merged-dedup.fastq > ../data07/bowtie-d/KFredrick007_C02-trim-merged-dedup.fastq.txt & 
bowtie -q -3 5 -S -k 10 ../ref/Ecoli_BW25113 ../data07/dedup/KFredrick007_C03-trim-merged-dedup.fastq > ../data07/bowtie-d/KFredrick007_C03-trim-merged-dedup.fastq.txt & 
wait
