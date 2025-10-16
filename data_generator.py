import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Constants for data generation
BRANCHES = ['KHONKAEN', 'PHUKET', 'CHIANGMAI', 'HATYAI', 'BANGKOK', 'PATTAYA']
BRANDS = ['PUMA', 'REEBOK', 'ADIDAS', 'NIKE', 'UNDER_ARMOUR', 'NEW_BALANCE']
PRODUCT_TYPES = ['SHOE', 'PANT', 'SHIRT', 'BAG', 'SOCK', 'HAT']
NUM_RECORDS = 10000000

def generate_order_no():
    """Generate a random order number"""
    return f"ORD{random.randint(100000, 999999)}"

def generate_customer_no():
    """Generate a random customer number"""
    return f"CUST{random.randint(1000, 9999)}"

def generate_sku(brand):
    """Generate a random SKU based on brand and product type"""
    product_type = random.choice(PRODUCT_TYPES)
    return f"{brand[:2].upper()}-{product_type}-{random.randint(1, 99):02d}"

def generate_dates(num_records):
    """Generate random dates within the year 2024"""
    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(
        days=random.randint(0, 364),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    ) for _ in range(num_records)]
    return dates

def generate_data(num_records=NUM_RECORDS):
    """Generate retail sales data"""
    data = {
        'order_no': [generate_order_no() for _ in range(num_records)],
        'amount': np.random.randint(100, 10000, num_records),
        'customer_no': [generate_customer_no() for _ in range(num_records)],
        'branch': np.random.choice(BRANCHES, num_records),
        'brand': np.random.choice(BRANDS, num_records),
        'quantity': np.random.randint(1, 10, num_records),
        'transaction_datetime': generate_dates(num_records)
    }
    
    # Generate SKUs based on brands
    data['sku'] = [generate_sku(brand) for brand in data['brand']]
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    print("Generating 10 million records...")
    df = generate_data()
    
    print("Saving sample to CSV...")
    df.head(1000).to_csv('retail_data_sample.csv', index=False)
    
    print("Data generation completed!")