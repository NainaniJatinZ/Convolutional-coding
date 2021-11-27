import numpy as np

import matplotlib.pyplot as plt

Data = np.load('./data/somaiya.npy')
print(Data)

# for i, v1 in enumerate(Data):
#     for j, v2 in enumerate(v1):
#         if v2 == 255:
#             Data[i, j] = 1
            
            
print(np.unique(Data))