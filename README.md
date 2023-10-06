# PandasPythonLearning
Our collaborative repository for studying Python Pandas, where we'll research and learn about this powerful data analysis library.

## Pandas Installation

``pip install pandas``

## Import Pandas

``import pandas as pd``

## Creating a DataFrame

```
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]} ``
df = pd.DataFrame(data)
```

## Viewing Data

```
# View the first few rows of the DataFrame
print(df.head())
# Check information about the DataFrame
print(df.info())
# Summary statistics of the DataFrame
print(df.describe())
```

## Selecting Data

```
# Selecting a column
names = df['Name']
# Selecting multiple columns
subset = df[['Name', 'Age']]
# Selecting rows based on a condition
adults = df[df['Age'] >= 30]
```


