#!/bin/bash
#SBATCH --job-name=B2-2
#SBATCH --output=B2-2.out
#SBATCH --time=04:00:00
#SBATCH --account=PAS0182  # Specify PI's account here
#SBATCH --ntasks=2                   # Number of parallel tasks (processes)
#SBATCH --cpus-per-task=24           # CPUs allocated per task (adjust as needed)
#SBATCH --constraint=48core

conda activate env1

bowtie -q -3 5 -S -k 10 ../ref/Ecoli_BW25113 ../data07/dedup/KFredrick007_B01-trim-merged-dedup.fastq > ../data07/bowtie/KFredrick007_B01-trim-merged-dedup.fastq.txt & 

bowtie -q -3 5 -S -k 10 ../ref/Ecoli_BW25113 ../data07/dedup/KFredrick007_B03-trim-merged-dedup.fastq > ../data07/bowtie/KFredrick007_B03-trim-merged-dedup.fastq.txt & 

wait
