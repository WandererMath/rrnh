#!/bin/bash
#SBATCH --job-name=2-trim
#SBATCH --output=2-exec_trim-output.txt
#SBATCH --time=04:00:00
#SBATCH --account=PAS0182  # Specify PI's account here
#SBATCH --ntasks=4                   # Number of parallel tasks (processes)
#SBATCH --cpus-per-task=12            # CPUs allocated per task (adjust as needed)
#SBATCH --constraint=48core



# Your job's commands go here
source ~/.bashrc
conda activate env1
cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o ./data/trim/A03-trim_R1.fastq -p ./data/trim/A03-trim_R2.fastq --discard-untrimmed --cores=12 --pair-filter=any --minimum-length=20 --maximum-length=55 -q 20,20 ./raw/A03_R1.fq ./raw/A03_R2.fq &
cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o ./data/trim/C03-trim_R1.fastq -p ./data/trim/C03-trim_R2.fastq --discard-untrimmed --cores=12 --pair-filter=any --minimum-length=20 --maximum-length=55 -q 20,20 ./raw/C03_R1.fq ./raw/C03_R2.fq &
cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o ./data/trim/B02-trim_R1.fastq -p ./data/trim/B02-trim_R2.fastq --discard-untrimmed --cores=12 --pair-filter=any --minimum-length=20 --maximum-length=55 -q 20,20 ./raw/B02_R1.fq ./raw/B02_R2.fq &
cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o ./data/trim/A01-trim_R1.fastq -p ./data/trim/A01-trim_R2.fastq --discard-untrimmed --cores=12 --pair-filter=any --minimum-length=20 --maximum-length=55 -q 20,20 ./raw/A01_R1.fq ./raw/A01_R2.fq &
cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o ./data/trim/C01-trim_R1.fastq -p ./data/trim/C01-trim_R2.fastq --discard-untrimmed --cores=12 --pair-filter=any --minimum-length=20 --maximum-length=55 -q 20,20 ./raw/C01_R1.fq ./raw/C01_R2.fq &
cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o ./data/trim/B01-trim_R1.fastq -p ./data/trim/B01-trim_R2.fastq --discard-untrimmed --cores=12 --pair-filter=any --minimum-length=20 --maximum-length=55 -q 20,20 ./raw/B01_R1.fq ./raw/B01_R2.fq &
cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o ./data/trim/B03-trim_R1.fastq -p ./data/trim/B03-trim_R2.fastq --discard-untrimmed --cores=12 --pair-filter=any --minimum-length=20 --maximum-length=55 -q 20,20 ./raw/B03_R1.fq ./raw/B03_R2.fq &
cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o ./data/trim/C02-trim_R1.fastq -p ./data/trim/C02-trim_R2.fastq --discard-untrimmed --cores=12 --pair-filter=any --minimum-length=20 --maximum-length=55 -q 20,20 ./raw/C02_R1.fq ./raw/C02_R2.fq &
cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o ./data/trim/A02-trim_R1.fastq -p ./data/trim/A02-trim_R2.fastq --discard-untrimmed --cores=12 --pair-filter=any --minimum-length=20 --maximum-length=55 -q 20,20 ./raw/A02_R1.fq ./raw/A02_R2.fq &


wait