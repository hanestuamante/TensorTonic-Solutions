import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Returns a float.
    """
    # Convert inputs to NumPy arrays
    x = np.asarray(x)
    y = np.asarray(y)
    
    # Calculate the sum of absolute differences
    distance = np.sum(np.abs(x - y))
    
    return float(distance)