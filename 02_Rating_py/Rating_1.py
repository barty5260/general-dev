import pandas as pd

# create a sample dataframe
df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [5, 10, 15],
    'C': [2, 4, 6],
    'D': [2, 5, 10]
})

# divide columns A, B, and C by column D, and create new columns E, F, and G
df['E'] = df['A'] / df['D']
df['F'] = df['B'] / df['D']
df['G'] = df['C'] / df['D']

# check if resulting columns breach more than 20, 15 or 10 points, and create new columns H, I, and J
df['H'] = (df['E'] > 20).astype(int)
df['I'] = (df['F'] > 15).astype(int)
df['J'] = (df['G'] > 10).astype(int)

# print the updated dataframe
print(df)
