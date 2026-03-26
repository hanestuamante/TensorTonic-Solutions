import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    O = np.array(C)
    
    row_sums = O.sum(axis=1)
    col_sums = O.sum(axis=0)
    n_total = O.sum()
    
    E = np.outer(row_sums, col_sums) / n_total
    
    chi2_stat = np.sum((O - E)**2 / E)
    
    return chi2_stat, E