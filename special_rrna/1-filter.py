with open("genomic.gtf","r") as fref, open("rna.txt","r") as fid, open("c1.gtf","w") as fw:
    rnas=[]
    for line in fid:
        rnas.append(line[:-1])
    for line in fref:
        if any(rna in line for rna in rnas) and "transcript" == line.split()[2]:
            fw.write(line)
