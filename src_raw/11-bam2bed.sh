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
bedtools intersect -a ../ref/true_genes_only.gtf -b ../data/bam/C01-bowtie1.bam -wa -wb > ../data/bed/C01-bowtie1.bed &
bedtools intersect -a ../ref/true_genes_only.gtf -b ../data/bam/C03-bowtie1.bam -wa -wb > ../data/bed/C03-bowtie1.bed &
bedtools intersect -a ../ref/true_genes_only.gtf -b ../data/bam/A01-bowtie1.bam -wa -wb > ../data/bed/A01-bowtie1.bed &
bedtools intersect -a ../ref/true_genes_only.gtf -b ../data/bam/C02-bowtie1.bam -wa -wb > ../data/bed/C02-bowtie1.bed &
bedtools intersect -a ../ref/true_genes_only.gtf -b ../data/bam/B03-bowtie1.bam -wa -wb > ../data/bed/B03-bowtie1.bed &
bedtools intersect -a ../ref/true_genes_only.gtf -b ../data/bam/A02-bowtie1.bam -wa -wb > ../data/bed/A02-bowtie1.bed &
bedtools intersect -a ../ref/true_genes_only.gtf -b ../data/bam/B01-bowtie1.bam -wa -wb > ../data/bed/B01-bowtie1.bed &
bedtools intersect -a ../ref/true_genes_only.gtf -b ../data/bam/A03-bowtie1.bam -wa -wb > ../data/bed/A03-bowtie1.bed &
bedtools intersect -a ../ref/true_genes_only.gtf -b ../data/bam/B02-bowtie1.bam -wa -wb > ../data/bed/B02-bowtie1.bed &
wait






