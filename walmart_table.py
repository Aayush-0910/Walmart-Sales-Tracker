import sqlite3
import pandas as pd


def display_table(table_name, conn):
    """
    Fetches data from a specified table and displays it as a DataFrame.
    
    Args:
        table_name (str): The name of the table to fetch.
        conn (sqlite3.Connection): SQLite connection object.
    """
    try:
     
        query = f"SELECT * FROM {table_name};"
        table_data = pd.read_sql_query(query, conn)
        
     
        if not table_data.empty:
            print(f"\nData from table '{table_name}':")
            print(table_data.to_string(index=False))  # Print DataFrame without row indices
        else:
            print(f"\nTable '{table_name}' is empty.")
    except Exception as e:
        print(f"Error fetching table '{table_name}': {e}")

def display_all_tables(conn):
    """
    Displays all the tables in the database.
    
    Args:
        conn (sqlite3.Connection): SQLite connection object.
    """
  
    tables = ["customers", "addresses", "employees", "orders", "sales_commissions"]
    for table in tables:
        display_table(table, conn)


if __name__ == "__main__":
    try:
   
        conn = sqlite3.connect('walmart_sales.db')
        

        display_all_tables(conn)
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    finally:
    
        conn.close()
