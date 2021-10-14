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
		MAX=`tmalign $f1 $f2 | awk '/TM-score=/'| awk '{print $2}' | sort -nr | head -1`
		line="$line$MAX,"
	done
	printf "${line%?}\n" >> simMat.csv
done
