#!/bin/bash
mkdir -p ./random_pdb_files
cd ./random_pdb_files
numStructures=50
while [ $(ls | wc -l) -lt $numStructures ]
do
  ID=""
  ID=$ID$(cat /dev/urandom | LC_CTYPE=C tr -dc '1-9'| fold -w ${1:-1} | head -n 1)
  ID=$ID$(cat /dev/urandom | LC_CTYPE=C tr -dc 'A-Z0-9'| fold -w ${1:-3} | head -n 1)
  echo $ID
  curl -O -L -f http://www.rcsb.org/pdb/files/$ID.pdb
done
