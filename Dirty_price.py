import pandas as pd
from datetime import datetime

df = pd.read_excel("Assignment 1 Data.xlsx")


df['days'] = (df.Date - datetime(2023, 9, 1)).dt.days

df['ratio'] = df['days']/365
print(df)

df2 = df[['Date', 'M24', 'S24', 'M25', 'S25', 'M26', 'S26','M27', 'S27', 'M28', 'S28', 'M29']].copy()
df2['M24'] = df2['M24']+(df['ratio']*0.0225*df2['M24'])
df2['S24'] = df2['S24']+(df['ratio']*0.015*df2['S24'])
df2['M25'] = df2['M25']+(df['ratio']*0.0125*df2['M25'])
df2['S25'] = df2['S25']+(df['ratio']*0.005*df2['S25'])
df2['M26'] = df2['M26']+(df['ratio']*0.0025*df2['M26'])
df2['S26'] = df2['S26']+(df['ratio']*0.01*df2['S26'])
df2['M27'] = df2['M27']+(df['ratio']*0.0125*df2['M27'])
df2['S27'] = df2['S27']+(df['ratio']*0.0275*df2['S27'])
df2['M28'] = df2['M28']+(df['ratio']*0.035*df2['M28'])
df2['S28'] = df2['S28']+(df['ratio']*0.0325*df2['S28'])
df2['M29'] = df2['M29']+(df['ratio']*0.04*df2['M29'])
print(df2)

df2.to_excel("dirty_prices.xlsx")

