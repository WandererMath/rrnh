# The .fq files have format error. 
# Remove first 3 lines


# Specify the directory you want to iterate through
directory=$DATA_DIR

# Iterate through all files in the directory
for file in "$directory"/*; do
  # Check if the file is a directory
  if [[ -d "$file" ]]; then
    continue
  fi

  # Do something with the file
  echo "Processing file: $file"
  cat $file | head -n 20 > ./check/$(basename $file)
done