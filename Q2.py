import pandas as pd
import datetime

# Load the CSV file
file_path = 'C:/Users/Admin/Desktop/DIY2_Divya/HR Employee Attrition.csv'
df = pd.read_csv(file_path)

# Add a column for the timestamp when the record was inserted
df['InsertedTimestamp'] = datetime.datetime.now()

# Initially, the last updated timestamp is the same as the inserted timestamp
df['LastUpdatedTimestamp'] = df['InsertedTimestamp']

# Save the modified DataFrame to a new CSV file
df.to_csv('C:/Users/Admin/Desktop/DIY2_Divya/HR_Employee_Attrition_with_Timestamps.csv', index=False)

# Display the first few rows of the modified DataFrame
print(df.head())
