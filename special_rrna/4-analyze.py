import os
import matplotlib.pyplot as plt
import numpy
import numpy as np
from scipy import stats

plt.rcParams['font.size'] = 15  # Global font size
plt.rcParams['figure.dpi'] = 300  # Global DPI

PATH="./feature-rrna-d"

def get_txt_files(folder_path):
    txt_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))
    return txt_files


def normalize(a):
    s=0
    for i in a:
        s+=i[1]
    for i in range(len(a)):
        a[i][1]/=s


files=get_txt_files(PATH)
results=[[],[],[]]
rnas=[]
labels=["A",'B','C']

for file in files:
    with open(file, "r") as f:
        counts=[]
        if "_A0" in file:
            label=0
        elif "_B0" in file:
            label=1
        else:
            label=2

        next(f)
        next(f)
        for i in range(7):
            #rna, count=next(f).split()
            line=next(f).split()
            rna=line[0]
            count=int(line[-1])
            count=[i,int(count)]
            counts.append(count)
            if len(rnas)<7:
                rnas.append(rna.split('_')[-1])
        normalize(counts)
        results[label].append(counts)

for group, i in zip(results, range(len(results))):
    group=numpy.array(group).transpose()

    plt.scatter(group[0], group[1],label=labels[i],s=10)
    plt.xticks(range(len(rnas)), rnas)
    plt.legend()

plt.savefig("rRNA.png", dpi=300)

RS01010=[numpy.array(results[i]).transpose()[1][0] for i in range(3)]
A_avg=sum(RS01010[0])/3
B_avg=sum(RS01010[1])/3
C_avg=sum(RS01010[2])/3
print(A_avg, B_avg, C_avg, sep='\n')

t_stat, p_value = stats.ttest_ind(RS01010[0], RS01010[2])
print("t-statistic:", t_stat)
print("p-value:", p_value)

plt.cla()
plt.figure(figsize=(8,6))
categories=["A (Wild Type)", "B (Knocked Out)", "C (Over Expressed)"]

for i, c in enumerate(categories):
    plt.scatter([i for _ in range(len(RS01010[i]))], RS01010[i], label=categories[i])
plt.xticks(range(len(categories)), categories)
plt.ylabel("rrnH  Frequency")
plt.title("Frequencies of rrnH")
plt.legend()
plt.savefig("Freq.png")
