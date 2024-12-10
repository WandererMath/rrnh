from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import mean, mode
import csv
import os
plt.rcParams['figure.dpi'] = 300
@dataclass
class Gene:
    pSD: int
    pMSD: int
    eSD: float
    eMSD: float

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
# [Stimulated, Reduced]
PATH_LISTS=["M.txt", "P.txt"]#, 'all_true_genes.txt']
PATHS=PATH_LISTS#[os.path.join("data", path) for path in PATH_LISTS]
FS='FS.csv'
GENES={}
ALPHA=0.5

with open(FS, 'r') as f:
    f=csv.reader(f)
    next(f)
    for line in f:
        try:
            tmp=line[1].split('\"')
            for elem in tmp:
                if "BW" in elem:
                    name=elem
            if name=="BW25113_RS11315":
                #breakpoint()
                print(1)
        except:
            #print(line)
            continue
        try:
            eSD=float(line[2])
        except:
            eSD=None
        try:
            eMSD=float(line[3])
        except:
            eMSD=None
        try:
            pSD=int(line[7])
            #print("Good")
        except:
            pSD=None
        try:
            pMSD=int(line[8])
        except:
            pMSD=None
        GENES[name]=Gene(pSD=pSD, pMSD=pMSD, eSD=eSD, eMSD=eMSD)

def main(PATH, label):
    my_genes=[]
    eSDs=[]
    eMSDs=[]
    pSDs=[]
    with open(PATH, 'r') as f:
        for line in f:
            my_genes.append(line.replace('\n', ''))
    for gene in my_genes:
        eSD=GENES[gene].eSD
        eMSD=GENES[gene].eMSD
        pSD=GENES[gene].pSD
        if eSD is not None:
            eSDs.append(eSD)
        if eMSD is not None:
            eMSDs.append(eMSD)
        if pSD is not None:
            pSDs.append(pSD)
    if label=='Stimulated':
        ax1.hist(eSDs,  label=label, alpha=ALPHA, density=True)
        ax2.hist(pSDs, label=label, alpha=ALPHA, density=True)
    else:
        ax1.hist(eSDs,  label=label, alpha=ALPHA, density=True)
        ax2.hist(pSDs, label=label, alpha=ALPHA, density=True)
    return eSDs, pSDs

'''
    plt.hist(eMSDs, bins=20)
    plt.title("MSD min E")
    plt.savefig(PATH+"Energy_MSD.PDF")
    plt.cla()
'''
labels=['Stimulated', 'Reduced']



E1, S1=main(PATHS[0], labels[0])
E2, S2=main(PATHS[1], labels[1])
#breakpoint()
_, p_E=stats.ranksums(E1, E2)
_, p_S=stats.ranksums(S1, S2)


ax1.set_title(f"ASD-SD Interaction Free Energy Distribution\nWilcoxon test p-value: {p_E}")
ax1.set_xlabel("Minimum Free Energy / (kcal/mol)")
ax1.set_ylabel("Density")
ax1.legend()

ax2.set_title(f"Spacing Between Start Codon and ASD-SD Matching Start Position\nWilcoxon test p-value: {p_S}")
ax2.set_xlabel("Optimum Spacing / Number of Nucleotides")
ax2.set_ylabel("Density")
ax2.legend()
plt.savefig("Energy_SD_2.PNG")
print(mean(S1)/mean(S2))