#!/bin/bash
mkdir -p ./random_pdb_structures
cd ./random_pdb_structures

numStructures=24
#numStructures=$1

while [ $(ls | wc -l) -lt $numStructures ]
do
  ID=""
  # Generates a random ID to attempt to download from PDB
  ID=$ID$(cat /dev/urandom | LC_CTYPE=C tr -dc '1-9'| fold -w ${1:-1} | head -n 1)
  ID=$ID$(cat /dev/urandom | LC_CTYPE=C tr -dc 'A-Z0-9'| fold -w ${1:-3} | head -n 1)
  echo $ID
  # Attempts to download the PDB structures for the corresponding ID. If the ID was
  # invalid continue.
  curl -O -L -f http://www.rcsb.org/pdb/files/$ID.pdb
done
