import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import sys
import os

# Arg1 input_dir, Arg2 output_dir
original_dir = os.getcwd()
os.chdir(sys.argv[1])
OUT_DIR=sys.argv[2]

PATH_AB="A-vs-B.csv"
PATH_AC="A-vs-C.csv"
#threshold=float(sys.argv[1])
threshold=1
def analysis(path):
    up=[]
    down=[]
    data=pd.read_csv(path)
    #print(data.head())
    #print(data["Unnamed: 0"][:5])
    #print(type(data["log2FoldChange"][2]))
    for i in range(len(data["Unnamed: 0"])):
        if data["log2FoldChange"][i]>=threshold and data["padj"][i]<=0.05 :
            gene=data["Unnamed: 0"][i]
            up.append(gene)
        if data["log2FoldChange"][i]<=-threshold and data["padj"][i]<=0.05 :
            gene=data["Unnamed: 0"][i]
            down.append(gene)
    return up, down


B_p, B_m=analysis(PATH_AB)
C_p, C_m=analysis(PATH_AC)
#print(B_p, "\n",B_m)

os.chdir(original_dir)
os.makedirs(OUT_DIR, exist_ok=True)
os.chdir(OUT_DIR)
venn2([set(B_p), set(C_m)],("B_upregulated", "C_downregulated"))
plt.plot()
plt.savefig("venn1.png")
plt.cla()

venn2([set(B_m), set(C_p)],("B_downregulated", "C_upregulated"))
plt.plot()
plt.savefig("venn2.png")
plt.cla()

venn2([set(B_m), set(C_m)],("B_downregulated", "C_downregulated"))
plt.plot()
plt.savefig("venn3.png")
plt.cla()

venn2([set(B_p), set(C_p)],("B_upregulated", "C_upregulated"))
plt.plot()
plt.savefig("venn4.png")
plt.cla()

def save(genes, path):
    with open (path, "w") as f:
        for gene in genes:
            f.write(gene+"\n")

genes=[B_p, B_m, C_p, C_m, set(B_p) & set(C_p), set(B_m) & set(C_m), set(B_p) & set(C_m), set(B_m) &set(C_p)]
paths=["B_p.txt", "B_m.txt", "C_p.txt", "C_m.txt", "B_p & C_p.txt", "B_m & C_m.txt", "B_p & C_m.txt", "B_m &C_p.txt"]

for gene, path in zip(genes, paths):
    save(gene, path)