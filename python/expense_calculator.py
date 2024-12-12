import psycopg2

# PostgreSQL setup
db_host = 'your-rds-endpoint'
db_name = 'expense_db'
db_user = 'your-db-user'
db_password = 'your-db-password'

def get_expenses_by_type():
    """Retrieve and calculate expenses by type."""
    connection = psycopg2.connect(
        host=db_host,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT expense_type, SUM(amount) 
        FROM expenses
        GROUP BY expense_type;
    """)
    
    expenses = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return expenses

def get_expenses_by_date():
    """Retrieve and calculate expenses by date."""
    connection = psycopg2.connect(
        host=db_host,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT date, SUM(amount) 
        FROM expenses
        GROUP BY date;
    """)
    
    expenses = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return expenses

def main():
    print("Expenses by Type:")
    expenses_by_type = get_expenses_by_type()
    for expense in expenses_by_type:
        print(f"{expense[0]}: ${expense[1]:.2f}")
    
    print("\nExpenses by Date:")
    expenses_by_date = get_expenses_by_date()
    for expense in expenses_by_date:
        print(f"{expense[0]}: ${expense[1]:.2f}")

if __name__ == '__main__':
    main()