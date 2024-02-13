import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    'x': [1, 2, 3, 4, 5],
    'y1': [2, 3, 5, 7, 11],
    'y2': [1, 4, 9, 16, 25]
}
df = pd.DataFrame(data)
print(df)
# Plot multiple columns on the same graph
df.plot(x='x', y=['y1', 'y2'], marker='o')

# Show the plot
#plt.show()
x = [1, 2, 3, 4]
y = sum(x[i] for i in range(len(x)))
print(y)
