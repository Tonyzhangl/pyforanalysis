# -*- conding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as pyt
from numpy import *


A = mat([[8, -3, 2], [4, 11, -1], [6, 3, 12]])
b = mat([20, 33, 36])
result = linalg.solve(A, b.T)
print result
