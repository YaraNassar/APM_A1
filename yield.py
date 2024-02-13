import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
df = pd.read_excel("dirty_prices.xlsx")

df['Date'] = df['Date'].astype(str)

df_2 = df[['Date']].copy()

L = []
for i in range(0, 11):
    def f_1(x):
        return (100 + (2.25/2))*np.exp(-x/6) - df['M24'][i]
    y = optimize.newton(f_1, 0.04)
    L.append(y)
df_2['2'] = L

L = []
for i in range(0, 11):
    def f_2(x):
        return (1.5/2)*np.exp(-x/6) + (100 + (1.5/2))*np.exp(-x*(8/12)) - df['S24'][i]
    y = optimize.newton(f_2, 0.03)
    L.append(y)
df_2['8'] = L

L = []
for i in range(0, 11):
    def f_3(x):
        return (1.25/2)*np.exp(-x/6) + (1.25/2)*np.exp(-x*(8/12)) + (100 + (1.25/2))*np.exp(-x*(14/12)) - df['M25'][i]
    y = optimize.newton(f_3, 0.04)
    L.append(y)
df_2['14'] = L

L = []
for i in range(0, 11):
    def f_4(x):
        return (0.5/2)*np.exp(-x/6) + (0.5/2)*np.exp(-x*(8/12)) + (0.5/2)*np.exp(-x*(14/12)) + (100 + (0.5/2))*np.exp(-x*(20/12)) - df['S25'][i]
    y = optimize.newton(f_4, 0.04)
    L.append(y)
df_2['20'] = L

L = []
for i in range(0, 11):
    def f_5(x):
        return (0.25/2)*np.exp(-x/6) + (0.25/2)*np.exp(-x*(8/12)) + (0.25/2)*np.exp(-x*(14/12)) + (0.25/2)*np.exp(-x*(20/12)) + (100 + (0.25/2))*np.exp(-x*(26/12)) - df['M26'][i]
    y = optimize.newton(f_5, 0.04)
    L.append(y)
df_2['26'] = L

L = []
for i in range(0, 11):
    def f_6(x):
        return (1/2)*np.exp(-x/6) + (1/2)*np.exp(-x*(8/12)) + (1/2)*np.exp(-x*(14/12)) + (1/2)*np.exp(-x*(20/12)) + (1/2)*np.exp(-x*(26/12)) + (100 + (1/2))*np.exp(-x*(32/12)) - df['S26'][i]
    y = optimize.newton(f_6, 0.04)
    L.append(y)
df_2['32'] = L

L = []
for i in range(0, 11):
    def f_7(x):
        return (1.25/2)*np.exp(-x/6) + (1.25/2)*np.exp(-x*(8/12)) + (1.25/2)*np.exp(-x*(14/12)) + (1.25/2)*np.exp(-x*(20/12)) + (1.25/2)*np.exp(-x*(26/12)) + (1.25/2)*np.exp(-x*(32/12)) + (100 + (1.25/2))*np.exp(-x*(38/12)) - df['M27'][i]
    y = optimize.newton(f_7, 0.04)
    L.append(y)
df_2['38'] = L

L = []
for i in range(0, 11):
    def f_8(x):
        return (2.75/2)*np.exp(-x/6) + (2.75/2)*np.exp(-x*(8/12)) + (2.75/2)*np.exp(-x*(14/12)) + (2.75/2)*np.exp(-x*(20/12)) + (2.75/2)*np.exp(-x*(26/12)) + (2.75/2)*np.exp(-x*(32/12)) + (2.75/2)*np.exp(-x*(38/12)) + (100 + (2.75/2))*np.exp(-x*(44/12)) - df['S27'][i]
    y = optimize.newton(f_8, 0.04)
    L.append(y)
df_2['44'] = L

L = []
for i in range(0, 11):
    def f_9(x):
        return (3.5/2)*np.exp(-x/6) + (3.5/2)*np.exp(-x*(8/12)) + (3.5/2)*np.exp(-x*(14/12)) + (3.5/2)*np.exp(-x*(20/12)) + (3.5/2)*np.exp(-x*(26/12)) + (3.5/2)*np.exp(-x*(32/12)) + (3.5/2)*np.exp(-x*(38/12)) + (3.5/2)*np.exp(-x*(44/12)) + (100 + (3.5/2))*np.exp(-x*(50/12)) - df['M28'][i]
    y = optimize.newton(f_9, 0.04)
    L.append(y)
df_2['50'] = L

L = []
for i in range(0, 11):
    def f_10(x):
        return (3.25/2)*np.exp(-x/6) + (3.25/2)*np.exp(-x*(8/12)) + (3.25/2)*np.exp(-x*(14/12)) + (3.25/2)*np.exp(-x*(20/12)) + (3.25/2)*np.exp(-x*(26/12)) + (3.25/2)*np.exp(-x*(32/12)) + (3.25/2)*np.exp(-x*(38/12)) + (3.25/2)*np.exp(-x*(44/12)) + (3.25/2)*np.exp(-x*(50/12)) + (100 + (3.25/2))*np.exp(-x*(56/12)) - df['S28'][i]
    y = optimize.newton(f_10, 0.04)
    L.append(y)
df_2['56'] = L

L = []
for i in range(0, 11):
    def f_11(x):
        return 2*np.exp(-x/6) + 2*np.exp(-x*(8/12)) + 2*np.exp(-x*(14/12)) + 2*np.exp(-x*(20/12)) + 2*np.exp(-x*(26/12)) + 2*np.exp(-x*(32/12)) + 2*np.exp(-x*(38/12)) + 2*np.exp(-x*(44/12)) + 2*np.exp(-x*(50/12)) + 2*np.exp(-x*(56/12)) + (102)*np.exp(-x*(62/12)) - df['M29'][i]
    y = optimize.newton(f_11, 0.04)
    L.append(y)
df_2['62'] = L

print(df_2)
df_2.to_excel('yields.xlsx')
#df_2.to_excel("transpose_yield.xlsx")