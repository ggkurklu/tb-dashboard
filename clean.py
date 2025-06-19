import pandas as pd
import numpy as np

df = pd.read_csv('TB_burden_countries_2025-06-18.csv')

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df = df.drop_duplicates()

for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

df['country'] = df['country'].str.strip().str.lower()

q99 = df['e_inc_100k'].quantile(0.99)
df = df[df['e_inc_100k'] <= q99]

df.rename(columns={
    'e_inc_100k': 'estimated_incidence_per_100k'
}, inplace=True)

df.to_csv('cleaned_data.csv', index=False)

print(" Data cleaning complete. Saved to 'cleaned_data.csv'")
