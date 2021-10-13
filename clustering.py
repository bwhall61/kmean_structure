import scipy.spatial.distance as ssd
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from numpy import genfromtxt
import pandas as pd
import numpy as np
import sys
import subprocess

def hierarchicalCluster(distanceMat, method):
    hierarchy = linkage(distanceMat,method)
    dendrogram(hierarchy,orientation="left",labels=distanceMat.columns)
    plt.show()


def main():
    method = sys.argv[-1]
    subprocess.call("./tmalignents.sh")
    m = pd.read_csv('final_val.csv')
    print(m)
    hierarchicalCluster(m,method)

if __name__ == '__main__':
    main()
