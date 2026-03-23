import numpy as np

def pearson_correlation(X):
    X = np.asarray(X, dtype=float)
    n_samples, n_features = X.shape
    
    mu = np.mean(X, axis=0)
    X_centered = X - mu
    std = np.std(X, axis=0)
    
    numerator = X_centered.T @ X_centered
    denominator = np.outer(std, std) * n_samples
    
    with np.errstate(divide='ignore', invalid='ignore'):
        R = numerator / denominator
    
    for i in range(n_features):
        if std[i] > 0:
            R[i, i] = 1.0
        else:
            R[i, i] = np.nan
            
    return R
