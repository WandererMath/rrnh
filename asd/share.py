from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class Gene:
    pSD: int
    pMSD: int
    eSD: float
    eMSD: float


GENES_NAME_ID={}
with open('id_name.txt') as f:
    for line in f:
        id, name=line.replace('\n','').split(',')
        if name=="WITHOUT NAME":
            pass
        else:
            GENES_NAME_ID[name]=id



GENES_ASD={}
with open('FS.csv', 'r') as f:
    next(f)
    for line in f:
        line=line.split(',')
        try:
            name=line[1].split()[1].replace(";", '').replace('"', '')
        except:
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
        except:
            pSD=None
        try:
            pMSD=int(line[8])
        except:
            pMSD=None
        GENES_ASD[name]=Gene(pSD=pSD, pMSD=pMSD, eSD=eSD, eMSD=eMSD)



if __name__=='__main__':
    #print(GENES_ASD)
    breakpoint()