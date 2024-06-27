import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Load the CSV file
file_path = 'C:/Users/Admin/Desktop/DIY2_Divya/HR Employee Attrition.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(df.head())

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Get summary statistics
summary_statistics = df.describe()
print("Summary statistics:\n", summary_statistics)

# Set up the matplotlib figure
plt.figure(figsize=(15, 10))

# Plot distributions of key numerical columns
plt.subplot(3, 3, 1)
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')

plt.subplot(3, 3, 2)
sns.histplot(df['DailyRate'], kde=True)
plt.title('Daily Rate Distribution')

plt.subplot(3, 3, 3)
sns.histplot(df['MonthlyIncome'], kde=True)
plt.title('Monthly Income Distribution')

# Visualize attrition by Job Satisfaction
plt.subplot(2, 3, 4)
sns.countplot(x='JobSatisfaction', hue='Attrition', data=df)
plt.title('Attrition by Job Satisfaction')

# Visualize attrition by Work Life Balance
plt.subplot(2, 3, 5)
sns.countplot(x='WorkLifeBalance', hue='Attrition', data=df)
plt.title('Attrition by Work Life Balance')

# Visualize attrition by Environment Satisfaction
plt.subplot(2, 3, 6)
sns.countplot(x='EnvironmentSatisfaction', hue='Attrition', data=df)
plt.title('Attrition by Environment Satisfaction')

plt.tight_layout()
plt.show()

# One-hot encoding for categorical variables
df_encoded = pd.get_dummies(df, columns=['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime'])

# Standardizing numerical features
# Selecting numerical features
numerical_features = ['Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 
                      'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany', 'YearsInCurrentRole', 
                      'YearsSinceLastPromotion', 'YearsWithCurrManager']

# Standardizing the numerical features
scaler = StandardScaler()
df_encoded[numerical_features] = scaler.fit_transform(df_encoded[numerical_features])

# Display the first few rows of the preprocessed data
print(df_encoded.head())
