import pandas as pd1
import mysql.connector


# Step 1: Extract
def extract_csv(file_path):
    print("Extracting data from CSV...")
    return pd1.read_csv(file_path)


# Step 2: Transform
def transform_data(df):
    print("Transforming data...")
    df = df.dropna(subset=['email'])  # Remove rows with missing email
    df.loc[:, 'customer_name'] = df['customer_name'].str.title()    # Normalize names
    df = df[df['purchase_amount'] > 1000]  # Filter for high-value customers
    return df


# Step 3: Load into MySQL
def load_to_mysql(df):
    print("Loading data to MySQL...")

    # Connect to MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='yourpassword',
        database='customer_sales'
    )
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_sales (
            customer_id INT,
            customer_name VARCHAR(100),
            email VARCHAR(100),
            purchase_amount FLOAT
        )
    """)

    # Insert data
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO customer_sales (customer_id, customer_name, email, purchase_amount)
            VALUES (%s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()


# Run ETL
def run_etl():
    file_path_of_customer_sales = '/Users/atverma/PycharmProjects/pythonProject/ETL_Week1/customer_sales.csv'  # Example CSV file path
    raw_df = extract_csv(file_path_of_customer_sales)
    clean_df = transform_data(raw_df)
    load_to_mysql(clean_df)
    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_etl()
