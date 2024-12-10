import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from itertools import combinations 
import os
import sys
from difflib import get_close_matches

'''

def best_match(string_set, target_string):
    """
    Returns the string in the set that best matches the given string.
    If no close match is found, returns None.
    
    Parameters:
        string_set (set): Set of strings to search for matches.
        target_string (str): The string to find the best match for.
        
    Returns:
        str or None: The closest match or None if no match is found.
    """
    # Convert set to a list and find the closest match
    matches = get_close_matches(target_string, string_set, n=1, cutoff=0.0)
    return matches[0] if matches else None
'''

def best_match(string_list, target):
    for s in string_list:
        if s in target:
            return s
# Example usage
if "data07" in sys.argv[1]:
    prefix='0'
else:
    prefix=''
string_set = [i+j for i in ["A", "B", "C"] for j in  [prefix+str(s) for s in range(1, 4)]]
print(string_set)

# Set global font size
plt.rcParams['font.size'] = 15  # Adjust the size as neededfrom difflib import get_close_matches
plt.rcParams['font.family'] = 'Times New Roman'
# Set DPI for figures
plt.rcParams['figure.dpi'] = 300  # Adjust the DPI as needed




os.chdir(sys.argv[1])
PATH="norm.csv"
TITLE="Normalized Gene Counts Scatter Plot"
PNG_DIR="PNG"

os.makedirs(PNG_DIR, exist_ok=True)

samples=[]
with open(PATH, "r") as f:
    line1=iter(next(f).split(","))
    next(line1)
    for s in line1:
        samples.append(s)

print(samples)
samples_index=[i for i in range(1,len(samples)+1)]
print(samples_index)
tasks=combinations(samples_index,2)

print(tasks)
def main(task):
    i1, i2=task
    


    X_ori=[]
    Y_ori=[]
    with open(PATH, "r") as f:
        next(f)
        for line in f:
            try:
                data=line.split(",")
                X_ori.append(float(data[i1]))
                Y_ori.append(float(data[i2]))
                if float(data[i1])==0 or float(data[i2])==0:
                    continue
                    
                #X.append(log(float(data[i1]),10))
                #Y.append(log(float(data[i2]),10))
            except:
                pass
    plt.figure(figsize=(9,9)) 
    plt.scatter(X_ori, Y_ori)
    correlation_coefficient, p_value = pearsonr(X_ori, Y_ori)
    
    label_x=best_match(string_set,samples[i1-1])
    label_y=best_match(string_set,samples[i2-1])
    plt.title(TITLE+"\nR="+str(correlation_coefficient))
    plt.xlabel("Sample "+label_x)
    plt.ylabel("Sample "+label_y)
    plt.xscale("log")
    plt.yscale("log")

    path_png=os.path.join(PNG_DIR,label_x+"-"+label_y+".PNG")
    plt.savefig(path_png)
    print(correlation_coefficient)

    plt.clf()
    plt.close()

for task in tasks:
    main(task)