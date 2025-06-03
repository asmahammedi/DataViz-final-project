import pandas as pd

# Load raw data from 'data.txt'
# Adjust delimiter if needed (e.g., delimiter='\t' for tab-separated)
df = pd.read_csv('data.txt')

# Preview first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset info: columns, data types, non-null counts
print("\nDataset info:")
print(df.info())

# Summary statistics for numeric columns
print("\nSummary statistics:")
print(df.describe())

# Check missing values per column
print("\nMissing values per column:")
print(df.isnull().sum())

# Check for duplicates
num_duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {num_duplicates}")

# Cleaning

# Fill missing numeric values with column mean
for col in df.select_dtypes(include='number').columns:
    mean_val = df[col].mean()
    df[col].fillna(mean_val, inplace=True)
    print(f"Filled missing values in '{col}' with mean: {mean_val}")

# Drop duplicate rows
if num_duplicates > 0:
    df.drop_duplicates(inplace=True)
    print(f"Dropped {num_duplicates} duplicate rows.")

# Convert date columns if you know the name of any date columns
# Example: if you have a column 'date', uncomment and adjust below
# df['date'] = pd.to_datetime(df['date'])

# Example calculated column:
# Assuming the dataset has a column named 'month' (sortable) and a numeric column 'sales'
if 'month' in df.columns and 'sales' in df.columns:
    df = df.sort_values('month')
    df['monthly_growth'] = df['sales'].pct_change() * 100
    print("Added 'monthly_growth' calculated column.")
else:
    print("Columns 'month' and/or 'sales' not found, skipping monthly growth calculation.")

# Export cleaned dataset to CSV for Power BI
output_file = 'cleaned_data.csv'
df.to_csv(output_file, index=False)
print(f"Cleaned data saved to '{output_file}'")
