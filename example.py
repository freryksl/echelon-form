import random
import numpy as np
from echelon import generator

def matrix(): # example matrix generated randomly
    rows = 5
    columns = 6
    nums = 2
    matrix = [[random.randint(0,nums) for i in range(columns)] for x in range(rows)]
    gen = generator(matrix)
    print("Row Echelon Form", "\n", np.array(gen.rowEchelon()),"\n")
    print("Reduced Row Echelon Form", "\n", np.array(gen.reducedRowEchelon()))

matrix()