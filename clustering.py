from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import sys
import subprocess

def hierarchicalCluster(simMat, method):
    hierarchy = linkage(simMat,method)
    dendrogram(hierarchy,orientation="left",labels=distanceMat.columns)
    plt.show()

def main():
    method = sys.argv[-1]
    subprocess.call(["./tmalignents.sh","./pdb_structures"])
    simMat = pd.read_csv('final_val.csv')
    hierarchicalCluster(simMat,method)

if __name__ == '__main__':
    main()
