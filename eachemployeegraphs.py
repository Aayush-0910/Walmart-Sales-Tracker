import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'Employee_Sales_Data.xlsx'  
df = pd.read_excel(file_path)


df['date'] = pd.to_datetime(df['date'])

# Extract year, month, and quarter
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['quarter'] = df['date'].dt.quarter

for employee in df['employee_name'].unique():
    employee_data = df[df['employee_name'] == employee]
 
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=employee_data, x='date', y='sales', marker='o')
    plt.title(f'Monthly Sales for {employee} (2023-2024)')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()

    # Quarterly Sales Bar Plot
    quarterly_sales = employee_data.groupby('quarter')['sales'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(data=quarterly_sales, x='quarter', y='sales')
    plt.title(f'Quarterly Sales for {employee} (2023-2024)')
    plt.xlabel('Quarter')
    plt.ylabel('Sales')
    plt.xticks(rotation=0)
    plt.grid()
    plt.tight_layout()
    plt.show()

# Commission Summary
commission_summary = df.groupby(['year', 'employee_name'])['commission'].sum().reset_index()
max_commission = commission_summary.loc[commission_summary.groupby('year')['commission'].idxmax()]

# Visualize Highest Commission Earned by Employees
plt.figure(figsize=(12, 6))
sns.barplot(data=max_commission, x='year', y='commission', hue='employee_name')
plt.title('Highest Commission Earned by Employees (2023-2024)')
plt.xlabel('Year')
plt.ylabel('Total Commission')
plt.legend(title='Employee Name')
plt.grid()
plt.tight_layout()
plt.show()