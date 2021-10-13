#!/bin/bash
FILES='./pdb_structures*'
for f1 in $FILES
do
	for f2 in $FILES

	do
		echo "Processing $f1 file..."
		tmalign $f1 $f2 > out.txt
		awk '/TM-score=/'  out.txt | awk '{print $2}' > outer.txt 
		awk -F"#" '{print $1, $0}' outer.txt  | sort -nr | head -1 > max.txt
		cat max.txt > final_val.txt
	done
done
