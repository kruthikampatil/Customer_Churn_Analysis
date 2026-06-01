Create database churn_project;
use churn_Project;

Show tables;

SELECT * 
FROM `customer_churn_dataset (1)`;

SELECT Gender, AVG(`Monthly Charges`) AS avg_monthly_charge
FROM `customer_churn_dataset (1)`
GROUP BY Gender;

SELECT `Internet Service`, COUNT(*) AS total_customers
FROM `customer_churn_dataset (1)`
GROUP BY `Internet Service`;

SELECT `Contract Type`, COUNT(*) AS churned_customers
FROM `customer_churn_dataset (1)`
WHERE Churn = 'Yes'
GROUP BY `Contract Type`;