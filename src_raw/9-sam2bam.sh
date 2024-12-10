#!/bin/bash
#SBATCH --output=2-exec_trim-output.txt
#SBATCH --time=04:00:00
#SBATCH --account=PAS0182  # Specify PI's account here
#SBATCH --ntasks=4                   # Number of parallel tasks (processes)
#SBATCH --cpus-per-task=12            # CPUs allocated per task (adjust as needed)
#SBATCH --constraint=48core



# Your job's commands go here
source ~/.bashrc
conda activate env1
samtools view -bS data/bowtie/C01-bowtie1.txt > data/bam/C01-bowtie1.bam &
samtools view -bS data/bowtie/C02-bowtie1.txt > data/bam/C02-bowtie1.bam &
samtools view -bS data/bowtie/B03-bowtie1.txt > data/bam/B03-bowtie1.bam &
samtools view -bS data/bowtie/C03-bowtie1.txt > data/bam/C03-bowtie1.bam &
samtools view -bS data/bowtie/A01-bowtie1.txt > data/bam/A01-bowtie1.bam &
samtools view -bS data/bowtie/A02-bowtie1.txt > data/bam/A02-bowtie1.bam &
samtools view -bS data/bowtie/B01-bowtie1.txt > data/bam/B01-bowtie1.bam &
samtools view -bS data/bowtie/A03-bowtie1.txt > data/bam/A03-bowtie1.bam &
samtools view -bS data/bowtie/B02-bowtie1.txt > data/bam/B02-bowtie1.bam &
wait




