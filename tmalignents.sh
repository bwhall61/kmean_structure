#!/bin/bash
PDBFILES="$1/*"
ls -1 "$1" | sed -e 's/\.pdb$//' | xargs | sed -e 's/ /,/g' > simMat.csv
for f1 in $PDBFILES
do
	line=""
	for f2 in $PDBFILES
	do
		tmalign $f1 $f2 > out.txt
		awk '/TM-score=/'  out.txt | awk '{print $2}' > outer.txt
		MAX=`awk -F"#" '{print $0}' outer.txt | sort -nr | head -1`
		line="$line${MAX},"
	done
	printf "${line%?}\n" >> simMat.csv
done
