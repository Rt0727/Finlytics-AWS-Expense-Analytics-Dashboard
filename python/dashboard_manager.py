import psycopg2
import json

# PostgreSQL setup
db_host = 'your-rds-endpoint'
db_name = 'expense_db'
db_user = 'your-db-user'
db_password = 'your-db-password'

def get_expenses_for_dashboard():
    """Get expense data for the dashboard."""
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
    
    # Format the result into a dictionary for the dashboard
    expenses_dict = {expense[0]: expense[1] for expense in expenses}
    return json.dumps(expenses_dict)

def main():
    dashboard_data = get_expenses_for_dashboard()
    print(f"Dashboard Data: {dashboard_data}")

if __name__ == '__main__':
    main()