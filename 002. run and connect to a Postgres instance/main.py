import psycopg2
from pprint import pprint as pp 

# PostgreSQL database configuration
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'yourpassword',  # Replace with your password
    'host': 'localhost',         
    'port': '5432',
}

try:
    # Establish a connection to the database
    conn = psycopg2.connect(**db_config)

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SQL query
    cursor.execute("SELECT version();")

    # Fetch and print the result
    db_version = cursor.fetchone()
    print(f"Database version: {db_version[0]}")
    
    #  --- perform queries here ---

except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()