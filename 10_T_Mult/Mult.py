import pandas as pd

# Creating two sample DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

# Perform matrix multiplication
result = df1.dot(df2.T)  # Transpose the second DataFrame using '.T'

print(result)
