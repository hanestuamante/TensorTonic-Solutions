import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    n = len(x)
    result = 0
    prob = 0
   
    for i in range(n):
        result += x[i] * p[i]
        prob += p[i]

    if prob != 1:
        raise ValueError
        
    return result
    pass
