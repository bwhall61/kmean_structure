from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from sklearn.cluster import SpectralClustering
import getopt
import sys
import pandas as pd
import subprocess

# Input: Similarity matrix, hierarchical clustering method to use. See Readme for options
# Output: Displays a dendrogram of the clusters
def hierarchicalCluster(simMat, method):
    hierarchy = linkage(simMat,method)
    dendrogram(hierarchy,orientation="left",labels=simMat.columns)
    plt.show()

# Input: Similarity matrix, number of clusters to use
# Output:
def spectralCluster(simMat,nClusters):
    clustering = SpectralClustering(n_clusters=nClusters,affinity='precomputed').fit(simMat)
    print(clustering.labels_)

# Input: Path to the folder containing PDB files to compare
# Output: Simialarity matrix with pariwise TM-scores from TMalign
# Runs the bash script tmalignments.sh which saves the simialrity matrix as simMat.csv
def genSimilarityMatrix(pdbFiles):
    subprocess.call(["./tmalignments.sh",pdbFiles])
    simMat = pd.read_csv('simMat.csv')
    return simMat

def usage():
    print('usage: clustering.py [-i pdbFiles_folder] [-m clustering_method] [-n nClusters] [-h]')

# Command line arguments: -i Folder containing all PDB files, -m method*, -n number of clusters
# Default: ./pdb_structures, ward hierarchical clustering, 2 clusters
# *spectral for spectral clustering, otherwise the algorithm for hierarchical clustering
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],"i:m:n:h",["input","method","nclusters","help"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    method = "ward"
    pdbFiles = "./pdb_structures"
    nClusters = 2

    for opt, arg in opts:
        if opt in ["-i","--input"]:
            pdbFiles = arg
        elif opt in ['-m',"--method"]:
            method = arg
        elif opt in ['-n','--nclusters']:
            nClusters = arg
        elif opt in ['-h','--help']:
            usage()
        else:
            usage()
            sys.exit(2)

    simMat = genSimilarityMatrix(pdbFiles)

    if(method == "spectral"):
        spectralCluster(simMat,nClusters)
    else:
        hierarchicalCluster(simMat,method)

if __name__ == '__main__':
    main()
