import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = 'C:/Users/Admin/Desktop/DIY2_Divya/HR Employee Attrition.csv'
df = pd.read_csv(file_path)

# Encode the 'Attrition' column to numeric
df['Attrition'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

# i) Sum of monthly income, average job satisfaction as per Job Role and Education Field
job_education_summary = df.groupby(['JobRole', 'EducationField']).agg(
    TotalMonthlyIncome=('MonthlyIncome', 'sum'),
    AverageJobSatisfaction=('JobSatisfaction', 'mean')
).reset_index()

# ii) Gender wise, job role wise average JobSatisfaction and Environment satisfaction
gender_jobrole_summary = df.groupby(['Gender', 'JobRole']).agg(
    AverageJobSatisfaction=('JobSatisfaction', 'mean'),
    AverageEnvironmentSatisfaction=('EnvironmentSatisfaction', 'mean')
).reset_index()

# iii) EducationField wise, JobRole wise average Hourly Rate, average MonthlyIncome, average JobSatisfaction
education_jobrole_summary = df.groupby(['EducationField', 'JobRole']).agg(
    AverageHourlyRate=('HourlyRate', 'mean'),
    AverageMonthlyIncome=('MonthlyIncome', 'mean'),
    AverageJobSatisfaction=('JobSatisfaction', 'mean')
).reset_index()

# iv) Department wise, gender wise average job satisfaction
department_gender_summary = df.groupby(['Department', 'Gender']).agg(
    AverageJobSatisfaction=('JobSatisfaction', 'mean')
).reset_index()

# v) Average breakdown of DistanceFromHome related to gender, department, and JobRole
distance_summary = df.groupby(['Gender', 'Department', 'JobRole']).agg(
    AverageDistanceFromHome=('DistanceFromHome', 'mean')
).reset_index()

# vi) Average monthly income by education and attrition
education_attrition_summary = df.groupby(['Education', 'Attrition']).agg(
    AverageMonthlyIncome=('MonthlyIncome', 'mean')
).reset_index()

# Visualization

# First Figure: Job Role and Education Field related visualizations
plt.figure(figsize=(9, 7))

# i) Sum of monthly income, average job satisfaction as per Job Role and Education Field
plt.subplot(2, 2, 1)
sns.barplot(data=job_education_summary, x='JobRole', y='TotalMonthlyIncome', hue='EducationField')
plt.title('Total Monthly Income by Job Role and Education Field')
plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper right')

plt.subplot(2, 2, 2)
sns.barplot(data=job_education_summary, x='JobRole', y='AverageJobSatisfaction', hue='EducationField')
plt.title('Average Job Satisfaction by Job Role and Education Field')
plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper right')

# ii) Gender wise, job role wise average JobSatisfaction and Environment satisfaction
plt.subplot(2, 2, 3)
sns.barplot(data=gender_jobrole_summary, x='JobRole', y='AverageJobSatisfaction', hue='Gender')
plt.title('Average Job Satisfaction by Gender and Job Role')
plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper right')

plt.subplot(2, 2, 4)
sns.barplot(data=gender_jobrole_summary, x='JobRole', y='AverageEnvironmentSatisfaction', hue='Gender')
plt.title('Average Environment Satisfaction by Gender and Job Role')
plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()

# Second Figure: Education Field, Department, and Distance From Home related visualizations
plt.figure(figsize=(9, 7))

# iii) EducationField wise, JobRole wise average Hourly Rate, average MonthlyIncome, average JobSatisfaction
plt.subplot(3, 2, 1)
sns.barplot(data=education_jobrole_summary, x='JobRole', y='AverageHourlyRate', hue='EducationField')
plt.title('Average Hourly Rate by Education Field and Job Role')
plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper right')

plt.subplot(3, 2, 2)
sns.barplot(data=education_jobrole_summary, x='JobRole', y='AverageMonthlyIncome', hue='EducationField')
plt.title('Average Monthly Income by Education Field and Job Role')
plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper right')

# iv) Department wise, gender wise average job satisfaction
plt.subplot(3, 2, 3)
sns.barplot(data=department_gender_summary, x='Department', y='AverageJobSatisfaction', hue='Gender')
plt.title('Average Job Satisfaction by Department and Gender')
plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper left')

# v) Average breakdown of DistanceFromHome related to gender, department, and JobRole
plt.subplot(3, 2, 4)
sns.barplot(data=distance_summary, x='JobRole', y='AverageDistanceFromHome', hue='Gender')
plt.title('Average Distance From Home by Gender, Department, and Job Role')
plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper right')

# vi) Average monthly income by education and attrition
plt.subplot(3, 2, 5)
sns.barplot(data=education_attrition_summary, x='Education', y='AverageMonthlyIncome', hue='Attrition')
plt.title('Average Monthly Income by Education and Attrition')
plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()
