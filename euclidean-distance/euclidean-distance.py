import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x_a = np.asarray(x)
    y_a = np.asarray(y)
    result = np.linalg.norm(x_a - y_a)
    return float(result)
    pass