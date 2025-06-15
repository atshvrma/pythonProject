import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Generate sample customer sales data
num_records = 1000

data = {
    'customer_id': [i for i in range(1, num_records + 1)],
    'name': [fake.name() for _ in range(num_records)],
    'email': [fake.email() for _ in range(num_records)],
    'signup_date': [fake.date_between(start_date='-5y', end_date='today') for _ in range(num_records)],
    'birthdate': [fake.date_between(start_date='-60y', end_date='today') for _ in range(num_records)],
    'last_purchase': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_records)],
    'total_spent': [round(random.uniform(100, 20000), 2) for _ in range(num_records)],
    'orders': [random.randint(1, 50) for _ in range(num_records)],
    'product_name': [fake.word() + random.choice(["-TV", "#LED", "!OLED", "_Smart"]) for _ in range(num_records)],
    'order_date': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_records)],
    'timestamp': [fake.date_time_this_year() for _ in range(num_records)]
}

df = pd.DataFrame(data)

# Save the CSV
csv_path = "customer_sales_data.csv"
df.to_csv(csv_path, index=False)

csv_path