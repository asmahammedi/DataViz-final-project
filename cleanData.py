import pandas as pd

# Load the CSV
df = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")

# Clean column names
df.columns = [col.strip().replace(" ", "_").replace("(", "").replace(")", "") for col in df.columns]

# Check for missing values
print(df.isnull().sum())

# Print column names for debugging
print("\nCleaned column names:")
print(df.columns.tolist())

# Convert data types
df['Year'] = df['Year'].astype(int)
df['Incident_Resolution_Time_in_Hours'] = df['Incident_Resolution_Time_in_Hours'].astype(float)
df['Financial_Loss_in_Million_$'] = df['Financial_Loss_in_Million_$'].astype(float)
df['Number_of_Affected_Users'] = df['Number_of_Affected_Users'].astype(float)

# Save cleaned version
df.to_csv("Cleaned_Cybersecurity_Threats.csv", index=False)
