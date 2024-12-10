export ref="./c2.gtf"
export data_folder="../data07/bowtie"
export OUTPUT="OUTPUT"

mkdir -p $OUTPUT
for file in $data_folder/*; do 
    #featureCounts -s 1 -M -Q 20 -T 5 -t transcript -g gene_id -a $ref -o "$OUTPUT/$(basename $file)" $file
    #"htseq-count " + bowtie_output_path+"/" + filename + " " + gtf_loc + " > " + out_loc
    htseq-count -s yes -t transcript --nproc 4 $file $ref > "$OUTPUT/$(basename $file)" 

  
done


#featureCounts -M -Q 20 -T 5 -t gene -g gene_id -a $ref -o $filename.txt $file