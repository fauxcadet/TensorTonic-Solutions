import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # ---- Edge cases ----
    if k < 0:
        return 0.0, 0.0
    if k >= n:
        # cdf becomes 1
        pmf = comb(n, n) * (p**n) * ((1-p)**0)
        return float(pmf), 1.0

    # ---- PMF ----
    pmf = comb(n, k) * (p**k) * ((1-p)**(n-k))

    # ---- CDF ----
    i = np.arange(0, k+1)
    probs = comb(n, i) * (p**i) * ((1-p)**(n-i))
    cdf = np.sum(probs)

    return float(pmf), float(cdf)
    pass