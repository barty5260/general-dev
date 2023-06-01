import pandas as pd

# Create a sample DataFrame
data = {'1st Column': [1, 2, 3],
        '2nd Column': [4, 5, 6],
        '3rd Column': [7, 8, 9]}
df = pd.DataFrame(data)

# Remove numbers from column headers
df.columns = df.columns.str.replace(r'\d+', '')

# Print the updated column headers
print(df.columns)
