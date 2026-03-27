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
        # Lọc các điểm thuộc cụm j bằng boolean masking
        cluster_points = X_arr[labels_arr == j]
        
        if len(cluster_points) > 0:
            # Tính trung bình cộng theo từng chiều (axis=0)
            centroid = np.mean(cluster_points, axis=0)
            # Chuyển từ NumPy array về list of floats
            new_centroids.append(centroid.tolist())
        else:
            # Nếu cụm rỗng, trả về vector không (danh sách các số 0.0)
            zero_vector = [0.0] * n_features
            new_centroids.append(zero_vector)
            
    return new_centroids