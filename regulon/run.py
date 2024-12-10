import json, csv
from scipy.stats import fisher_exact

# Path to the JSON file
json_file_path = "operon.json"

# Load the JSON file and save it in a dictionary
with open(json_file_path, 'r') as file:
    data_dict = json.load(file)


data=data_dict["data"]["getAllOperon"]["data"]

# Print the dictionary to verify
print(data[0])

# You can now use `data_dict` to access the JSON data
first_genes=[]
for operon in data:
    target=operon["transcriptionUnits"][0]['name']
    if target is None:
        continue
    #breakpoint()
    first_gene=None
    for i, e in enumerate(target):
        if e.isupper():
            first_gene=target[:i+1]
            break
    if first_gene is None:
        first_gene=target
    #print(first_gene)
    first_genes.append(first_gene)

#breakpoint()
#---------------------------------



# Path to your CSV file
csv_file_path = "id_name.txt"

# Initialize an empty dictionary
data_dict = {}

# Read the CSV file row by row
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        key, value = row[0], row[1]  # First element as key, second as value
        if not value=="WITHOUT NAME":
            data_dict[key] = value

# Print the resulting dictionary
#print(data_dict)

ID_NAME=data_dict

#--------------------------------------------


PATH1='BmCp.txt'
PATH2='BpCm.txt'

def read_list(path):
    gene_list=[]
    with open(path, 'r') as f:
        for line in f:
            line=line.replace("\n", '')
            try:
                name=ID_NAME[line]
                gene_list.append(name)
            except KeyError:
                pass
    return gene_list

LIST1=read_list(PATH1)
LIST2=read_list(PATH2)
#print(LIST1)
#print(first_genes)
def count(gene_list):
    c=0
    for gene in gene_list:
        if gene in first_genes:
            c+=1
    return c

c1=count(LIST1)
c2=count(LIST2)
print(c1/len(LIST1), c2/len(LIST2),'\n', len(first_genes)/len(ID_NAME))

table1=[[c1, len(LIST1)-c1],
        [len(first_genes), len(ID_NAME)-len(first_genes)]]


table2=[[c2, len(LIST1)-c2],
        [len(first_genes), len(ID_NAME)-len(first_genes)]]

table3=[[c1, len(LIST1)-c1],
        [c2, len(LIST1)-c2]]

result1 = fisher_exact(table1, alternative='two-sided')
result2 = fisher_exact(table2, alternative='two-sided')
result3 = fisher_exact(table3, alternative='two-sided')
print(result1, result2, result3, sep='\n')