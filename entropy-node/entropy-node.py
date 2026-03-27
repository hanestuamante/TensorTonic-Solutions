import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node. 
    Ensures non-negativity and numerical stability.
    """
    n = len(y)
    if n <= 1: 
        return 0.0

    counts = {}
    for label in y:
        counts[label] = counts.get(label, 0) + 1

    # 2. Tính xác suất p_i
    # Lưu ý: Không nên lấy 1/j trực tiếp vào dict nếu muốn tính chuẩn p*log(p)
    probs = [count / n for count in counts.values()]
    arr = np.array(probs)

    # 3. Tính Entropy với cơ chế chống lỗi log(0)
    # Thêm epsilon (1e-15) để đảm bảo log2(p) không bao giờ bị âm vô cùng
    # và kết quả cuối cùng không bị âm do sai số dấu phẩy động
    entropy = -np.sum(arr * np.log2(arr + 1e-15))

    # Đảm bảo không trả về -0.0 do sai số máy tính
    return max(0.0, float(entropy))
