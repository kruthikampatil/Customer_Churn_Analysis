import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Data Analyst Projects\Customer_Churn_Analysis_Project 2\Python\Customer_Churn_csv.csv") # Read CSV File

print(df.head()) # Terminal Output
print(df['Gender'].value_counts())
print(df['Contract Type'].value_counts())

plt.figure(figsize=(8,6)) # Charts in One Screen

plt.subplot(2,2,1) # Pie Chart
df['Churn'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Churn")

plt.subplot(2,2,2) # Gender Chart
df['Gender'].value_counts().plot(kind='bar')
plt.title("Gender")

plt.subplot(2,2,3) # Contract Type Chart
df['Contract Type'].value_counts().plot(kind='bar')
plt.title("Contract")

plt.subplot(2,2,4) # Monthly Charges Chart
df['Monthly Charges'].plot(kind='hist')
plt.title("Monthly Charges Distribution")

plt.tight_layout()
plt.show()