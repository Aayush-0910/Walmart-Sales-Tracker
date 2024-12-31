Overview
Walmart Sales Tracker is a Python-based project that uses a database to track customer purchases, employee commissions, and sales performance for Walmart stores in six major Indian cities: Delhi, Bangalore, Mumbai, Hyderabad, Chennai, and Kolkata. The project provides insightful data visualizations to analyze employee sales performance for the years 2023 and 2024.

Features
Database Design:
Tables to store data for customers, their addresses, employees, order/purchase details, and sales commissions.
Data Generation:
Includes at least 10 purchase records for each month of 2023 and 2024.
Visualizations:
Monthly and quarterly sales for each employee.
Insights into top-performing employees by total commission earned.
Project Structure
data/: Contains SQL scripts for database schema and sample data.
visuals/: Includes visualizations like monthly sales, quarterly sales, and top commissions.
scripts/: Python scripts to create the database, populate it, and generate visuals.
README.md: Documentation for the project.
requirements.txt: Lists Python dependencies.
Database Design
Tables
Customers: Stores customer details (e.g., ID, name).
Addresses: Stores customer address details (e.g., city, street).
Employees: Stores employee details (e.g., ID, name).
Orders: Tracks purchases (e.g., order ID, customer ID, employee ID, date, amount).
Sales_Commissions: Tracks commission details (e.g., employee ID, order ID, commission amount).
Requirements
Python 3.8+
SQLite (or any relational database)
Libraries:
pandas
matplotlib
sqlite3
Install dependencies using the following command:
pip install -r requirements.txt

Usage
Set up the database:
Run the script to create the database schema:
python scripts/create_database.py

Generate data:
Populate the database with sample data:
python scripts/generate_data.py

Create visualizations:
Generate sales and commission visualizations:
python scripts/generate_visuals.py

Analyze data:
Check the visuals/ folder for the generated charts:

Monthly sales (monthly_sales.png)
Quarterly sales (quarterly_sales.png)
Top commissions (top_commissions.png)
Visualizations
Monthly Sales per Employee:
A bar chart showing employee sales trends for each month.

Quarterly Sales per Employee:
A grouped bar chart summarizing quarterly sales.

Top Commission Earners:
A pie chart displaying employees with the highest commissions earned.

Future Enhancements
Add support for real-time data updates.
Build an interactive dashboard using libraries like Dash or Plotly.
Integrate machine learning to predict future sales trends.
Contributing
Contributions are welcome! Fork the repository, make your changes, and submit a pull request. For major changes, open an issue to discuss your suggestions.

License
This project is licensed under the MIT License. See the LICENSE file for details.

