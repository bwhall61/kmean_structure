#!/bin/bash
FILES='./pdb_structures/*'
ls -1 './pdb_structures' | sed -e 's/\.pdb$//' | xargs | sed -e 's/ /,/g' > final_val.csv
for f1 in $FILES
do
	line=""
	for f2 in $FILES
	do
		tmalign $f1 $f2 > out.txt
		awk '/TM-score=/'  out.txt | awk '{print $2}' > outer.txt
		MAX=`awk -F"#" '{print $0}' outer.txt | sort -nr | head -1`
		line="$line${MAX},"
	done
	printf "${line%?}\n" >> final_val.csv
done
