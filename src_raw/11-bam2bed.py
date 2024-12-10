import os

PATH_SAM="../data/bam"
PATH_BAM="../data/bed"
OUTPUT_SCRIPT="11-bam2bed.txt"

sams_base=[f for f in os.listdir(PATH_SAM) if os.path.isfile(os.path.join(PATH_SAM, f))]
sams = [os.path.join(PATH_SAM, f) for f in sams_base]

print(sams)

sams_base_tmp=iter(sams_base)
with open(OUTPUT_SCRIPT, "w") as f:
    for sam in sams:
        sam_base=next(sams_base_tmp)

        bam=os.path.join(PATH_BAM, sam_base[:-4]+".bed")
        cmd="bedtools intersect -a ../ref/true_genes_only.gtf -b {} -wa -wb > {} &\n".format(sam, bam)
        f.write(cmd)
    f.write("wait\n")
    
