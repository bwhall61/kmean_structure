import scipy.spatial.distance as ssd
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import numpy as np
import sys

def hierarchicalCluster(distanceMat, method):
    distArray = ssd.squareform(distanceMat)
    hierarchy = linkage(distArray,method)
    dendrogram(hierarchy)
    plt.show()


def main():
    matrixFile = sys.argv[-2]
    method = sys.argv[-1]
    m = np.loadtxt(matrixFile)
    m = 1 - m.reshape(8,8)
    print(m)
    hierarchicalCluster(m,method)

if __name__ == '__main__':
    main()
