import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel("spot_rates.xlsx")
print(df)
df = df.drop(df.columns[0], axis = 1)

df['Date'] = df['Date'].astype(str)
df_2 = df[['Date']].copy()

#yearly spot rates from interpolation 
df_2['1yr'] = df['8'] + 4*np.divide((df['14'] - df['8']), 6)
df_2['2yr'] = df['20'] + 4*np.divide((df['26'] - df['20']), 6)
df_2['3yr'] = df['32'] + 4*np.divide((df['38'] - df['32']), 6)
df_2['4yr'] = df['44'] + 4*np.divide((df['50'] - df['44']), 6)

#forward rates 
df_3 = df[['Date']].copy()

df_3['1yr-1yr'] = df_2['1yr']
df_3['1yr-2yr'] = df_2['2yr']*2 - df_2['1yr']
df_3['1yr-3yr'] = (df_2['3yr']*3 - df_2['1yr'])/2
df_3['1yr-4yr'] = (df_2['2yr']*4 - df_2['1yr'])/3

df_3.to_excel("forward_rates.xlsx")
