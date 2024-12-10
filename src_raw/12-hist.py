import matplotlib.pyplot as plt
import sys
PATH=sys.argv[1]

X=[]
with open(PATH, "r") as f:
    for line in f:
        try:
            line=line.split()
            start=int(line[-5])
            end=int(line[-4])
            X.append(end-start)
        except:
            pass

plt.rcParams['figure.dpi'] = 300


plt.hist(X, density=True, bins=20)
plt.title("Ribosome Profiling - Protein Genes mRNA Reads Length Distribution")
plt.ylabel("Frequency")
plt.xlabel(f"Sample {PATH.split("/")[-1].split("-")[0]}")
plt.savefig("../data08/histogram/"+PATH.split("/")[-1].split("-")[0]+".png")