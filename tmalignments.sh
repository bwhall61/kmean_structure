#!/bin/bash

<< 'COMMENT'
This script computes the tmalign score for all pairs of proteins contained in a directory (of type PDB).
The input is the folder of PDB files.
The output is a similarity matrix of filetype csv.

References:
Y. Zhang, J. Skolnick, TM-align: A protein structure alignment algorithm based on TM-score, Nucleic Acids Research, 33: 2302-2309
COMMENT

PDBFILES="$1/*"
ls -1 "$1" | sed -e 's/\.pdb$//' | xargs | sed -e 's/ /,/g' > simMat.csv
for f1 in $PDBFILES
do
	line=""
	for f2 in $PDBFILES
	do
		SC1=`tmalign $f1 $f2 | awk '/TM-score=/'| awk '{print $2}' | head -1`
		SC2=`tmalign $f1 $f2 | awk '/TM-score=/'| awk '{print $2}' | tail -1`
		AVG=$(echo "scale=5;($SC1 + $SC2) / 2" | bc)
		line="$line$AVG,"
	done
	printf "${line%?}\n" >> simMat.csv
done
