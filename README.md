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

Defaults: numStructures: 24

Note that if you run this script twice it will not add additional pdB files to the
folder if there are already numStructures in the folder.

References:
[1] Daniel Mullner, “Modern hierarchical, agglomerative clustering algorithms”, arXiv:1109.2378v1.
[2] Ziv Bar-Joseph, David K. Gifford, Tommi S. Jaakkola, “Fast optimal leaf ordering for hierarchical clustering”, 2001. Bioinformatics DOI:10.1093/bioinformatics/17.suppl_1.S22
[3] Y. Zhang, J. Skolnick, TM-align: A protein structure alignment algorithm based on TM-score, Nucleic Acids Research, 33: 2302-2309 (2005)
[4] Normalized cuts and image segmentation, 2000 Jianbo Shi, Jitendra Malik http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.160.2324
[5] A Tutorial on Spectral Clustering, 2007 Ulrike von Luxburg http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.165.9323
[6] Multiclass spectral clustering, 2003 Stella X. Yu, Jianbo Shi https://www1.icsi.berkeley.edu/~stellayu/publication/doc/2003kwayICCV.pdf
