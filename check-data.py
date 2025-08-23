import pandas as pd

# load the CSV file
df = pd.read_csv("data/2000-25-data.csv")

print(df.head())         # shows first 5 rows
print(df.columns.tolist())  # shows all column names

print(df.info())         # shows datatypes and missing values
print(df.describe())     # summary stats (avg, min, max)
print(df['FullTimeResult'].value_counts())  # counts of H/D/A
print(df['HomeTeam'].unique()[:10])  # first 10 unique teams

print(df.isnull().sum())