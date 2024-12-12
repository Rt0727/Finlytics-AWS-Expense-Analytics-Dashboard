import psycopg2
import boto3
import csv
from io import StringIO

# AWS S3 Setup
s3_client = boto3.client('s3')
bucket_name = 'your-s3-bucket-name'
file_key = 'financial_data.csv'

# PostgreSQL setup
db_host = 'your-rds-endpoint'
db_name = 'expense_db'
db_user = 'your-db-user'
db_password = 'your-db-password'

def fetch_data_from_s3(bucket, key):
    """Fetch CSV file from S3."""
    s3_object = s3_client.get_object(Bucket=bucket, Key=key)
    return s3_object['Body'].read().decode('utf-8')

def import_data_to_postgresql(csv_data):
    """Import data into PostgreSQL."""
    connection = psycopg2.connect(
        host=db_host,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()
    
    # Assuming CSV headers are 'expense_type', 'amount', 'date'
    csv_reader = csv.reader(StringIO(csv_data))
    next(csv_reader)  # Skip header row

    for row in csv_reader:
        cursor.execute("""
            INSERT INTO expenses (expense_type, amount, date)
            VALUES (%s, %s, %s);
        """, (row[0], row[1], row[2]))
    
    connection.commit()
    cursor.close()
    connection.close()

def main():
    data = fetch_data_from_s3(bucket_name, file_key)
    import_data_to_postgresql(data)

if __name__ == '__main__':
    main()