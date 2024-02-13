import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("forward_rates.xlsx")
df.plot(x='Date', y=["2024-01-08", "2024-01-09", "2024-01-10", "2024-01-11","2024-01-12", "2024-01-15","2024-01-16", "2024-01-17","2024-01-18", "2024-01-19","2024-01-22"], marker='o')
plt.xlabel('Years')
plt.ylabel('Forward Rates')
plt.title('1-Year Forward Curve')
plt.legend(fontsize='small')
plt.show()
