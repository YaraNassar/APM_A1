import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel("dirty_prices.xlsx")

df['Date'] = df['Date'].astype(str)
#print(df)
df_2 = df[['Date']].copy()

cr = [2.25, 1.5, 1.25, 0.5, 0.25, 1, 1.25, 2.75, 3.5, 3.25, 4]
time = [ 2/12, 8/12, 14/12, 20/12, 26/12, 32/12, 38/12, 44/12, 50/12, 56/12, 62/12]
bonds = ['M24', 'S24','M25', 'S25','M26', 'S26','M27', 'S27','M28', 'S28','M29']
Months = ['2', '8', '14', '20', '26', '32', '38', '44', '50', '56', '62']
for i in range(0, len(Months)):
    df_2[Months[i]] = (-np.log((df[bonds[i]] + (cr[i]/2)*sum(-np.exp(-df_2[Months[j]]*time[j]) for j in range(i)))/(100+(cr[i]/2))))/time[i]

print(df_2)
df_2.to_excel("spot_rates.xlsx")


