import os
PATH="../data08/bed"

beds=[os.path.join(PATH, f) for f in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, f))]

with open("13.txt","w") as f:
    for bed in beds:
        f.write("python 12-hist.py {} &\n".format(bed))
    f.write("wait\n")