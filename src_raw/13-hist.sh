#!/bin/bash
#SBATCH --output=13
#SBATCH --time=04:00:00
#SBATCH --account=PAS0182  # Specify PI's account here
#SBATCH --ntasks=9                   # Number of parallel tasks (processes)
#SBATCH --cpus-per-task=2            # CPUs allocated per task (adjust as needed)
#SBATCH --constraint=48core



# Your job's commands go here
source ~/.bashrc
conda activate env_plot
python 12-hist.py ../data08/bed/A01-bowtie1.bed &
python 12-hist.py ../data08/bed/C01-bowtie1.bed &
python 12-hist.py ../data08/bed/A02-bowtie1.bed &
python 12-hist.py ../data08/bed/C03-bowtie1.bed &
python 12-hist.py ../data08/bed/C02-bowtie1.bed &
python 12-hist.py ../data08/bed/B03-bowtie1.bed &
python 12-hist.py ../data08/bed/B01-bowtie1.bed &
python 12-hist.py ../data08/bed/A03-bowtie1.bed &
python 12-hist.py ../data08/bed/B02-bowtie1.bed &
wait






