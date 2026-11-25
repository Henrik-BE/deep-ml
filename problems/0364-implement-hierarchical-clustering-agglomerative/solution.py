import numpy as np

def distance(x1, x2, linkage):
    if linkage == "single":
        min_dist = float("inf")
        for x1_elem in x1:
            for x2_elem in x2:
                i = 0
                dist = 0
                while i < len(x1_elem):
                    dist += (x1_elem[i] - x2_elem[i])**2
                    i+=1
                dist = np.sqrt(dist)
                min_dist = min(min_dist, dist)
        
        return min_dist

    elif linkage == "complete":
        max_dist = 0
        for x1_elem in x1:
            for x2_elem in x2:
                i = 0
                dist = 0
                while i < len(x1_elem):
                    dist+= (x1_elem[i] - x2_elem[i])**2
                    i+=1
                dist = np.sqrt(dist)
                max_dist = max(max_dist, dist)

        return max_dist

    elif linkage == "average":
        dists = []
        for x1_elem in x1:
            for x2_elem in x2:
                i = 0
                dist = 0
                while i < len(x1_elem):
                    dist+= (x1_elem[i] - x2_elem[i])**2
                    i+=1
                dist = np.sqrt(dist)
                dists.append(dist)
        
        return np.average(dists)
    
    else:
        return 67



def agglomerative_clustering(X: list, n_clusters: int, linkage: str = 'single') -> list:
    """
    Perform agglomerative hierarchical clustering.
    
    Args:
        X: Data points, shape (n_samples, n_features)
        n_clusters: Number of clusters to form
        linkage: 'single', 'complete', or 'average'
    
    Returns:
        List of cluster labels for each sample
    """
    
    clusters = [[x] for x in X]

    while len(clusters) != n_clusters and len(clusters) > 1:
        i = 0
        min_distance = float("inf")
        x1 = []
        x2 = []
        while i < len(clusters):
            j = 0
            while j < len(clusters):
                if j == i:
                    j+=1
                    continue

                dist = distance(clusters[i], clusters[j], linkage)
                if dist < min_distance:
                    min_distance = dist
                    x1 = clusters[i]
                    x2 = clusters[j]
                j+=1
            i+=1

        for elem in x2:
            x1.append(elem)
        clusters.remove(x2)

    cluster_indexes = []
    for point in X:
        i = 0
        while i < len(clusters):
            if point in clusters[i]:
                cluster_indexes.append(i)
            i+=1

    return cluster_indexes