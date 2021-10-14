# kmean_structure
This program uses clustering algorithms to cluster protein structures according to
pairwise TM-scores. It currently has options to use spectral and hierarchical clustering
algorithms.

To run: python clustering.py -i Folder containing all PDB files, -m method, -n number of clusters

Methods: Spectral: spectral
         Hierarchical: single, complete, weighted, centroid, median, ward,

Defaults: Folder: ./pdb_structures
          Method: ward
          Clusters: 2


We also include a bash script that will download random PDB structures to test
the algorithms.

To run: bash genRandomStructures.sh numStructures

Defaults: numStructures: 50

Note that if you run this script twice it will not add additional pdB files to the
folder if there are already numStructures in the folder.

References:
[1] Daniel Mullner, “Modern hierarchical, agglomerative clustering algorithms”, arXiv:1109.2378v1.
[2] Ziv Bar-Joseph, David K. Gifford, Tommi S. Jaakkola, “Fast optimal leaf ordering for hierarchical clustering”, 2001. Bioinformatics DOI:10.1093/bioinformatics/17.suppl_1.S22
