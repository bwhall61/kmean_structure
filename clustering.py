import scipy.spatial.distance as ssd
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from numpy import genfromtxt
import numpy as np
import sys
import subprocess

def hierarchicalCluster(distanceMat, method):
    distArray = ssd.squareform(distanceMat)
    hierarchy = linkage(distArray,method)
    dendrogram(hierarchy)
    plt.show()


def main():
    method = sys.argv[-1]
    subprocess.call("./tmalignents.sh")
    m = 1-genfromtxt('final_val.csv',delimiter=',')
    hierarchicalCluster(m,method)

if __name__ == '__main__':
    main()
