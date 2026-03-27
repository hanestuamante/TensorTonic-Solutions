import numpy as np
def k_means_centroid_update(X, labels, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    X_arr = np.array(X)
    labels_arr = np.array(labels)
    
    n_features = X_arr.shape[1]
    new_centroids = []

    for j in range(k):
        cluster_points = X_arr[labels_arr == j]
        
        if len(cluster_points) > 0:
            centroid = np.mean(cluster_points, axis=0)
            new_centroids.append(centroid.tolist())
        else:
            zero_vector = [0.0] * n_features
            new_centroids.append(zero_vector)
            
    return new_centroids