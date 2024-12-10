import matplotlib.pyplot as plt

PATH="data/bed/A01-bowtie1.bed"

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

plt.hist(X)
plt.savefig("A1.png")