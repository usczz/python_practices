"""
hilbert matrix using numpy, contains:
    - hilb(n, m): generate Hilbert Matrix of size (n, m)

"""

import numpy as np
from math import factorial


def binomial(n, k):
    """ binomial(n, k): Generate Binomial Coefficient for nCk """
    if k < 0 or k > n:
        return 0
    if k == n or k == 0:
        return 1
    return factorial(n) // (factorial(k) * factorial(n - k))


def hilb(n, m=0):
    """
    hilb Hilbert Matrix.
    :param n: number of rows
    :param m: number of cols

    hilb(n,m) is the n-by-m matrix with elements 1/(i + j - 1)
    """
    if n < 1 or m < 0:
        raise ValueError("Matrix size must be one or greater")
    elif n == 1 and (m == 0 or m == 1):
        return np.array([[1]])
    elif m == 0:
        m = n
    # np.arange(0,m) is [0, 1, 2, ..., m - 1]
    # np.arange(0,m)[:,np.newaxis] is [[0] [1]]
    # [1, 2, 3] + [[1] [2] [3]] = [[2, 3, 4] [3, 4, 5], [4, 5, 6]]
    v = np.arange(1, n + 1) + np.arange(0, m)[:, np.newaxis]
    return 1. / v
