import sys
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
    
    # default seed
    seed = 555

    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = int(sys.argv[p+1])
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed] change seed value" % sys.argv[0])
        print
        sys.exit(1)

    np.random.seed(seed)
    N = 500 
    Nmeas = 100
    X = np.zeros((N, 2))
    X[:100, :] = np.random.randn(100, 2) + np.array([0, 0])
    X[100:200, :] = np.random.randn(100, 2) + np.array([3, 3])
    X[200:300, :] = np.random.randn(100, 2) + np.array([-3, 3])
    X[300:400, :] = np.random.randn(100, 2) + np.array([-3, -3])  
    X[400:, :] = np.random.randn(100, 2) + np.array([3, -3])  

    real_cluster_centers = np.array([[3, 3], [3, -3], [0, 0], [-3, 3], [-3, -3]])

    # plot data
    plt.scatter(X[:, 0], X[:, 1], alpha=0.5)
    plt.show()

    # defines clusters from data
    kmeans = KMeans(n_clusters=5, n_init=10, random_state=0).fit(X)  # Updated nclusters to 5

    # plots clusters
    plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, alpha=0.5)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='o', s=100, linewidths=2,color='crimson',edgecolor='black')
    plt.show()

    print("The Calcuated Center of the Clusters:")
    print(kmeans.cluster_centers_)

    print("The Real Center of the Clusters:")
    print(real_cluster_centers)

