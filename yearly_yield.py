import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel("yields.xlsx")
print(df)
df = df.drop(df.columns[0], axis = 1)

df['Date'] = df['Date'].astype(str)
df_2 = df[['Date']].copy()

#yearly spot rates from interpolation 
df_2['1'] = df['8'] + 4*np.divide((df['14'] - df['8']), 6)
df_2['2'] = df['20'] + 4*np.divide((df['26'] - df['20']), 6)
df_2['3'] = df['32'] + 4*np.divide((df['38'] - df['32']), 6)
df_2['4'] = df['44'] + 4*np.divide((df['50'] - df['44']), 6)
df_2['5'] = df['56'] + 4*np.divide((df['62'] - df['56']), 6)

print(df_2)

df_2.to_excel('yearly_yields.xlsx')