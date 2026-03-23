import numpy as np

def pearson_correlation(X):
    X = np.asarray(X, dtype=float)
    n_samples, n_features = X.shape
    
    # 1. Tính toán sai số và độ lệch chuẩn
    mu = np.mean(X, axis=0)
    X_centered = X - mu
    std = np.std(X, axis=0)
    
    # 2. Tính tử số và mẫu số
    numerator = X_centered.T @ X_centered
    denominator = np.outer(std, std) * n_samples
    
    # 3. Tính toán R (sẽ tạo ra NaN tại các vị trí mẫu số = 0)
    with np.errstate(divide='ignore', invalid='ignore'):
        R = numerator / denominator
    
    # 4. Xử lý đường chéo theo logic đặc biệt:
    # Chỉ giữ 1.0 nếu std > 0, nếu std == 0 thì để là NaN
    for i in range(n_features):
        if std[i] > 0:
            R[i, i] = 1.0
        else:
            R[i, i] = np.nan
            
    return R

# Test với X = [[1, 5], [2, 5], [3, 5]]
# Cột 1: std > 0 -> R[0,0] = 1.0
# Cột 2: std = 0 -> R[1,1] = NaN