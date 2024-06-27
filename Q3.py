import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import datetime

# Load the CSV file
file_path = 'C:/Users/Admin/Desktop/DIY2_Divya/HR Employee Attrition.csv'
df = pd.read_csv(file_path)

# Add timestamp columns
df['InsertedTimestamp'] = datetime.datetime.now()
df['LastUpdatedTimestamp'] = df['InsertedTimestamp']

# Encode categorical variables
df_encoded = pd.get_dummies(df, columns=['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime'])

# Standardize numerical features
numerical_features = ['Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 
                      'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany', 'YearsInCurrentRole', 
                      'YearsSinceLastPromotion', 'YearsWithCurrManager']

scaler = StandardScaler()
df_encoded[numerical_features] = scaler.fit_transform(df_encoded[numerical_features])

# Feature selection
features = df_encoded.drop(columns=['Attrition', 'EmployeeCount', 'EmployeeNumber', 'StandardHours', 'Over18', 'InsertedTimestamp', 'LastUpdatedTimestamp'])
target = df_encoded['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Classification Model: Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(classification_rep)
print('Confusion Matrix:')
print(conf_matrix)

# Identifying the best-fitted cause of Employee dissatisfaction
coefficients = pd.DataFrame(model.coef_[0], features.columns, columns=['Coefficient'])
coefficients = coefficients.sort_values(by='Coefficient', ascending=False)
print('Coefficients indicating the cause of employee dissatisfaction:')
print(coefficients)
