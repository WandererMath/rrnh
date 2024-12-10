OFFSET1=1000
OFFSET2=1023

with open("c1.gtf","r") as fr, open("d2.gtf","w") as fw:
    for line in fr:
        line=line.split(";")[0]
        entry=line.split()
        #entry[2]='exon'
        print(int(entry[4])-int(entry[3]))
        if entry[6]=="-":
            entry[3]=str(int(entry[4])-OFFSET2)
            entry[4]=str(int(entry[4])-OFFSET1)
        else:
            entry[4]=str(int(entry[3])+OFFSET2)
            entry[3]=str(int(entry[3])+OFFSET1)
            
        # Change TAB after gene_id to space
        # Otherwise featureCounts can't parse correctly and gives unhelpful error info
        # htseq-count can work but it's super slow
        fw.write("\t".join(entry[:-1])+" "+entry[-1]+";\n")