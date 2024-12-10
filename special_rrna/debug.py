import os
import matplotlib.pyplot as plt
import numpy

PATH="./OUTPUT-d"

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

D1=[numpy.array(results[i]).transpose()[1][1] for i in range(3)]
D2=[numpy.array(results[i]).transpose()[1][-1] for i in range(3)]
D1=D1[1][1]
D2=D2[1][1]

print(D1, D2, D2/D1)

D1=[numpy.array(results[i]).transpose()[1][1] for i in range(3)]
D2=[numpy.array(results[i]).transpose()[1][-1] for i in range(3)]
D1=D1[0][1]
D2=D2[0][1]

print(D1, D2, D2/D1)
