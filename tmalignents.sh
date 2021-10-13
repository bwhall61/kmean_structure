#!/bin/bash
FILES='./pdb_structures/*'
echo -n > final_val.txt
for f1 in $FILES
do
	for f2 in $FILES

	do
		tmalign $f1 $f2 > out.txt
		awk '/TM-score=/'  out.txt | awk '{print $2}' > outer.txt
		MAX=`awk -F"#" '{print $0}' outer.txt | sort -nr | head -1`
		echo -e ${MAX}
		echo -e ${MAX} >> final_val.txt
	done
done
