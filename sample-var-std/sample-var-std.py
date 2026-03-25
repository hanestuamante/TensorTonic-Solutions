import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    n = len(x)
    x_ = np.sum(x)/n
    sum = 0
    for i in range(n):
         sum += (x[i] - x_)**2

    var = (1 / (n - 1)) * sum
    std = np.sqrt(var)
    return var, std
  