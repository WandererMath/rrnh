import os

PATH_SAM="data/bowtie"
PATH_BAM="data/bam"
OUTPUT_SCRIPT="9-sam2bed.txt"

sams_base=[f for f in os.listdir(PATH_SAM) if os.path.isfile(os.path.join(PATH_SAM, f))]
sams = [os.path.join(PATH_SAM, f) for f in sams_base]

print(sams)

sams_base_tmp=iter(sams_base)
with open(OUTPUT_SCRIPT, "w") as f:
    for sam in sams:
        sam_base=next(sams_base_tmp)

        bam=os.path.join(PATH_BAM, sam_base[:-4]+".bam")
        cmd="samtools view -bS {} > {} &\n".format(sam, bam)
        f.write(cmd)
    f.write("wait\n")
    
