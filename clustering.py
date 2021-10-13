import scipy.spatial.distance as ssd
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import numpy as np

def hierarchicalCluster(distanceMat, method):
    distArray = ssd.squareform(distanceMat)
    hierarchy = linkage(distArray,method)
    dendrogram(hierarchy)
    plt.show()

test = np.array([[0,1,4,5],[1,0,3,4],[4,3,0,1],[5,4,1,0]])
hierarchicalCluster(test,'ward')
