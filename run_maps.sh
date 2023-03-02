#!/bin/sh

# Loop over all the 2020 files, run map.py on each and remove their extension
for file in /data/Twitter\ dataset/geoTwitter20*
do
    outputfile=$(basename "$file")
    nohup ./src/map.py --input_path="$file" > "outputs/${outputfile%.*}" & 
done


