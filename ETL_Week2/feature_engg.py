import pandas as pd

df = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'last_purchase': ['2024-12-01', '2025-01-15', '2025-06-01']
})

df['last_purchase'] = pd.to_datetime(df['last_purchase'])
df['days_since_last'] = (pd.Timestamp.now() - df['last_purchase']).dt.days


# print time since last purchase 
print(df)