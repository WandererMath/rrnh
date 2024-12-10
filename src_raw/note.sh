#Bedtools intersect
bowtie-build GCF_000750555.1_ASM75055v1_genomic.fna Ecoli_BW25113
samtools view -bS alignment.sam > alignment.bam
tar -xvjf filename.tar.bz2
tar -xzvf filename.tar.gz

bedtools intersect -a genes_only.gtf -b ../data/bam/A01-bowtie1.bam -wa -wb > ../data/bed/A01-bowtie1.bed
#ECOCYC
#IGV