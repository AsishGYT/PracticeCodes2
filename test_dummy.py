from scipy.spatial.distance import cosine
import numpy as np
from numpy.linalg import norm

import pandas as pd


def cosine_similarity(a, b):
    matrix = pd.DataFrame({"A": a, "B": b})
    matrix = matrix.dropna(axis = 0, how='any')
    print(matrix)
    # a = matrix[['A']]
    # b = matrix[['B']]
    # return 1 - (cosine(a, b))


cosine_similarity([1, np.nan, 3, 4], 
                [np.nan, 2, 4, 1] )


                #1,3,4
                #2,4,1

                #3,4
                #4,1

                