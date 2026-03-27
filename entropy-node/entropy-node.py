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
        
    probs = [count / n for count in counts.values()]
    arr = np.array(probs)


    entropy = -np.sum(arr * np.log2(arr + 1e-15))


    return max(0.0, float(entropy))
