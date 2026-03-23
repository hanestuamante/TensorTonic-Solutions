import numpy as np

def binning(values, num_bins):
    """
    Assign each value to an equal-width bin (0 to num_bins-1).
    """
    values = np.array(values)
    min_val = np.min(values)
    max_val = np.max(values)
    
    w = (max_val - min_val) / num_bins
    
    bins = np.floor((values - min_val) / w).astype(int)
    
    return (np.clip(bins, 0, num_bins - 1)).tolist()