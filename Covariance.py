import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
df = pd.read_excel("yy_transpose.xlsx")
array = df.to_numpy()

log_returns = np.zeros((5, 9))
for i in range(len(array)):
    for j in range(len(array[i])-1):
        log_returns[i][j] = math.log(array[i][j]/array[i][j+1])
#print(log_returns)
C1 = np.cov(log_returns)
#print(C1)

w1, v1 = np.linalg.eig(C1)
#print(w1)
print(v1)

df_2 = pd.read_excel('fr.xlsx')

array_2 = df_2.to_numpy()

log_returns_2 = np.zeros((4, 9))
for i in range(len(array_2)):
    for j in range(len(array_2[i])-1):
        log_returns_2[i][j] = math.log(array_2[i][j]/array_2[i][j+1])

C2 = np.cov(log_returns_2)
#print(C2)

w2, v2 = np.linalg.eig(C2)
#print(w2)
#print(v2)