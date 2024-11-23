import sqlite3
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect('walmart_sales.db')
cursor = conn.cursor()

# Define the database tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address_id INTEGER,
    FOREIGN KEY(address_id) REFERENCES addresses(address_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS addresses (
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    employee_id INTEGER,
    purchase_date DATE,
    price REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales_commissions (
    commission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    month INTEGER,
    year INTEGER,
    commission REAL,
    FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
);
''')

# Populate tables with data
cities = ["Delhi", "Bangalore", "Mumbai", "Hyderabad", "Chennai", "Kolkata"]
months = list(range(1, 13))
years = [2023, 2024]

# Insert addresses
for city in cities:
    cursor.execute("INSERT INTO addresses (city) VALUES (?)", (city,))

# Insert customers and link them with an address
for city in cities:
    for i in range(100):  # 100 customers per city
        cursor.execute("INSERT INTO customers (name, address_id) VALUES (?, ?)",
                       (f"Customer_{city}_{i+1}", cities.index(city) + 1))

# Insert employees
for city in cities:
    for i in range(10):  # 10 employees per city
        cursor.execute("INSERT INTO employees (name, city) VALUES (?, ?)",
                       (f"Employee_{city}_{i+1}", city))

# Insert orders and commissions for 2023-2024
for year in years:
    for month in months:
        for _ in range(10):  # At least 10 purchases per month
            customer_id = random.randint(1, 600)
            employee_id = random.randint(1, 60)
            price = round(random.uniform(10, 500), 2)
            date_str = f"{year}-{month:02d}-01"
            cursor.execute("INSERT INTO orders (customer_id, employee_id, purchase_date, price) VALUES (?, ?, ?, ?)",
                           (customer_id, employee_id, date_str, price))

        # Calculate and insert monthly commissions for each employee
        for employee_id in range(1, 61):
            total_sales = cursor.execute(
                "SELECT SUM(price) FROM orders WHERE employee_id = ? AND strftime('%Y', purchase_date) = ? AND strftime('%m', purchase_date) = ?",
                (employee_id, str(year), str(month).zfill(2))
            ).fetchone()[0] or 0
            commission = total_sales * 0.05  # Assuming 5% commission
            cursor.execute("INSERT INTO sales_commissions (employee_id, month, year, commission) VALUES (?, ?, ?, ?)",
                           (employee_id, month, year, commission))

# Commit changes
conn.commit()

##
# Step 4: Generate Visualizations

# 1. Sales per month and quarter per employee
#for employee_id in range(1, 61):
    # Monthly sales
#    monthly_sales = pd.read_sql_query(
#         "SELECT month, SUM(commission) as total_commission FROM sales_commissions WHERE employee_id = ? AND year IN (2023, 2024) GROUP BY year, month",
#         conn, params=(employee_id,)
#     )
    
#     plt.figure(figsize=(12, 6))
#     plt.plot(monthly_sales['month'], monthly_sales['total_commission'], marker='o', linestyle='-')
#     plt.title(f'Monthly Sales for Employee {employee_id} (2023-2024)')
#     plt.xlabel('Month')
#     plt.ylabel('Total Commission')

    # # Quarterly sales
    # monthly_sales['quarter'] = (monthly_sales['month'] - 1) // 3 + 1
    # quarterly_sales = monthly_sales.groupby('quarter').sum()
#     plt.xticks(months, [calendar.month_abbr[m] for m in months])
#     plt.show()
    
    # plt.figure(figsize=(12, 6))
    # plt.bar(quarterly_sales.index, quarterly_sales['total_commission'])
    # plt.title(f'Quarterly Sales for Employee {employee_id} (2023-2024)')
    # plt.xlabel('Quarter')
    # plt.ylabel('Total Commission')
    # plt.show()
##
# 2. Highest commission recipient
highest_commission_2023 = pd.read_sql_query(
    "SELECT employee_id, SUM(commission) as total_commission FROM sales_commissions WHERE year = 2023 GROUP BY employee_id ORDER BY total_commission DESC LIMIT 1",
    conn
)
highest_commission_2024 = pd.read_sql_query(
    "SELECT employee_id, SUM(commission) as total_commission FROM sales_commissions WHERE year = 2024 GROUP BY employee_id ORDER BY total_commission DESC LIMIT 1",
    conn
)

read_customer_table = pd.read_sql_query(
    "SELECT * FROM customers",
    conn
)

read_address_table = pd.read_sql_query(
    "SELECT * FROM addresses",
    conn
)

read_employees_table = pd.read_sql_query(
    "SELECT * FROM employees",
    conn
)

read_orders_table = pd.read_sql_query(
    "SELECT * FROM orders",
    conn
)

read_sales_commissions_table = pd.read_sqlṇ_query(
    "SELECT * FROM sales_commissions",
    conn
)

print("Employee with the highest commission in 2023:", highest_commission_2023)
print("Employee with the highest commission in 2024:", highest_commission_2024)
print("Customer table data:", read_customer_table)
#print("Customer table data:", read_customer_table)
print("Address table data:", read_address_table)
print("Employee table data:", read_employees_table)
print("Orders table data:",read_orders_table)
print("sales_commission table data:",read_sales_commissions_table)

# Close connection
conn.close()
