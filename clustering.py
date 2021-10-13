from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import getopt
import sys
import pandas as pd
import subprocess

def hierarchicalCluster(simMat, method):
    print(method)
    hierarchy = linkage(simMat,method)
    dendrogram(hierarchy,orientation="left",labels=simMat.columns)
    plt.show()

def genSimilarityMatrix(pdbFiles):
    subprocess.call(["./tmalignments.sh",pdbFiles])
    simMat = pd.read_csv('simMat.csv')
    return simMat

def usage():
    print('usage: clustering.py [-i pdbFiles_folder] [-m clustering_method [-h]')

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],"i:m:h:",["input","method","help"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    method = "ward"
    pdbFiles = "./pdb_structures"

    for opt, arg in opts:
        if opt in ["-i","--input"]:
            pdbFiles = arg
        elif opt in ['-m',"--method"]:
            method = arg
        elif opt in ['-h','--help']:
            usage()
        else:
            usage()
            sys.exit(2)

    simMat = genSimilarityMatrix(pdbFiles)
    hierarchicalCluster(simMat,method)

if __name__ == '__main__':
    main()
