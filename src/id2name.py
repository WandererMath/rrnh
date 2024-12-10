import os, sys
from share import GENES_ID_NAME
def get_files_base(path, end):
# List all files ending with .txt
    return [file for file in os.listdir(path) if file.endswith(end)]


PATH=sys.argv[1]

def main(input, output):
    with open(input, 'r') as fr, open(output, 'w') as fw:
        for line in fr:
            line=line.replace('\n', '')
            try:
                sym=GENES_ID_NAME[line]
            except KeyError:
                #breakpoint()
                continue
            if not sym=="WITHOUT NAME":
                fw.write(sym+"\n")

files_base=get_files_base(PATH, '.txt')
files=[os.path.join(PATH, file) for file in files_base]
for file, file_base in zip(files, files_base):
    file_out=os.path.join(PATH,file_base.split('.')[0]+".symbol")
    main(file, file_out)