import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_retail_data(seed=42, num_records=1600):
    np.random.seed(seed)
    
    # Date range: Jan 1, 2023 to Dec 31, 2025
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2025, 12, 31)
    days_range = (end_date - start_date).days
    
    # Generate dates with Q4 / holiday seasonality weighting
    random_days = np.random.randint(0, days_range, size=num_records)
    dates = [start_date + timedelta(days=int(d)) for d in random_days]
    
    # Introduce seasonality weight: increase end-of-year sales (Nov-Dec)
    extra_dates = []
    for _ in range(350):
        year = np.random.choice([2023, 2024, 2025], p=[0.3, 0.35, 0.35])
        month = np.random.choice([11, 12], p=[0.45, 0.55])
        day = np.random.randint(1, 29)
        extra_dates.append(datetime(year, month, day))
    
    all_dates = dates + extra_dates
    all_dates.sort()
    total_samples = len(all_dates)
    
    # Product Taxonomy
    products_db = {
        'Electronics': {
            'Smartphones': [('UltraPhone 15 Pro', 999.00), ('Galaxy S24 Ultra', 1199.00), ('Pixel 8 Pro', 899.00)],
            'Laptops': [('MacBook Pro 16"', 2499.00), ('Dell XPS 15', 1799.00), ('ThinkPad X1 Carbon', 1599.00)],
            'Audio': [('Noise-Canceling Headphones', 299.00), ('Wireless Earbuds Pro', 199.00), ('Bluetooth Party Speaker', 149.00)],
            'Accessories': [('USB-C Fast Charger 65W', 39.00), ('Ergonomic Wireless Mouse', 49.00), ('4K HDMI Cable 6ft', 19.00)]
        },
        'Clothing & Apparel': {
            'Men\'s Wear': [('Classic Cotton Denim Jacket', 89.00), ('Tailored Slim Fit Suit', 299.00), ('Casual Oxford Shirt', 45.00)],
            'Women\'s Wear': [('Floral Summer Sundress', 65.00), ('Designer Trench Coat', 189.00), ('High-Waisted Skinny Jeans', 59.00)],
            'Footwear': [('Performance Running Shoes', 129.00), ('Leather Ankle Boots', 149.00), ('Canvas Casual Sneakers', 55.00)],
            'Activewear': [('Breathable Gym Leggings', 42.00), ('Moisture-Wicking Athletic Hoodie', 68.00), ('Seamless Sports Bra', 35.00)]
        },
        'Home & Kitchen': {
            'Appliances': [('Digital Espresso Machine', 499.00), ('Air Fryer XL 5.8Qt', 119.00), ('Smart Robot Vacuum', 349.00)],
            'Cookware': [('Cast Iron Dutch Oven 6Qt', 85.00), ('Non-Stick Cookware 10-Pc Set', 159.00), ('Chef Stainless Steel Knife', 49.00)],
            'Furniture': [('Ergonomic Mesh Office Chair', 229.00), ('Minimalist Wooden Desk', 279.00), ('Modern Velvet Armchair', 310.00)],
            'Home Decor': [('Handwoven Wool Area Rug', 175.00), ('Aromatherapy Essential Oil Diffuser', 29.00), ('LED Smart Ambience Lamp', 45.00)]
        },
        'Beauty & Personal Care': {
            'Skincare': [('Hydrating Facial Serum 50ml', 48.00), ('Anti-Aging Night Cream', 62.00), ('SPF 50 Mineral Sunscreen', 28.00)],
            'Haircare': [('Ionic Hair Dryer 1800W', 89.00), ('Nourishing Argan Hair Oil', 32.00), ('Ceramic Flat Iron Hair Straightener', 75.00)],
            'Fragrance': [('Luxury Eau de Parfum 100ml', 120.00), ('Fresh Citrus Cologne', 85.00), ('Floral Mist Body Spray', 22.00)]
        },
        'Books & Stationery': {
            'Fiction': [('Bestselling Mystery Novel', 18.00), ('Sci-Fi Epic Hardcover', 24.00), ('Romantic Comedy Paperback', 14.00)],
            'Non-Fiction': [('Atomic Habits & Self-Help', 22.00), ('Financial Freedom Handbook', 26.00), ('World History Illustrated', 35.00)],
            'Stationery': [('Premium Leather Journal', 25.00), ('Calligraphy Pen Set', 30.00), ('Minimalist Planner 2025', 19.00)]
        }
    }
    
    # Flatten categories for sampling
    cat_list = list(products_db.keys())
    cat_weights = [0.30, 0.25, 0.22, 0.13, 0.10]
    
    records = []
    
    # Generate customers pool (500 distinct customers)
    num_customers = 500
    customer_ids = [f"CUST-{1000 + i}" for i in range(num_customers)]
    customer_genders = np.random.choice(['Male', 'Female', 'Non-binary'], size=num_customers, p=[0.48, 0.49, 0.03])
    customer_ages = np.random.randint(18, 72, size=num_customers)
    customer_segments = np.random.choice(['Consumer', 'Corporate', 'Home Office'], size=num_customers, p=[0.55, 0.30, 0.15])
    
    cust_map = {}
    for i in range(num_customers):
        cust_map[customer_ids[i]] = {
            'gender': customer_genders[i],
            'age': customer_ages[i],
            'segment': customer_segments[i]
        }
        
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America']
    region_weights = [0.42, 0.28, 0.20, 0.10]
    
    payment_methods = ['Credit Card', 'PayPal', 'Debit Card', 'Apple Pay', 'Bank Transfer']
    payment_weights = [0.45, 0.25, 0.15, 0.10, 0.05]

    for idx, dt in enumerate(all_dates):
        trans_id = f"TXN-{2023000 + idx + 1}"
        c_id = np.random.choice(customer_ids)
        c_info = cust_map[c_id]
        
        category = np.random.choice(cat_list, p=cat_weights)
        subcat = np.random.choice(list(products_db[category].keys()))
        prod_tuple = products_db[category][subcat][np.random.randint(0, len(products_db[category][subcat]))]
        prod_name, base_price = prod_tuple
        
        # Quantity based on category
        if category in ['Electronics', 'Home & Kitchen']:
            quantity = np.random.choice([1, 2, 3], p=[0.75, 0.20, 0.05])
        else:
            quantity = np.random.choice([1, 2, 3, 4, 5], p=[0.40, 0.30, 0.15, 0.10, 0.05])
            
        # Discount policy: 0%, 5%, 10%, 15%, 20%, 25%, 30%
        # Higher discounts on clothing/decor, lower on electronics
        if category in ['Clothing & Apparel', 'Home & Kitchen']:
            discount = np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], p=[0.25, 0.20, 0.20, 0.15, 0.10, 0.06, 0.04])
        else:
            discount = np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20], p=[0.50, 0.25, 0.15, 0.07, 0.03])
            
        # Unit price variation (± 5%)
        unit_price = round(base_price * np.random.uniform(0.95, 1.05), 2)
        total_sales = round(quantity * unit_price * (1.0 - discount), 2)
        
        # Profit Calculation: Base cost is 45-65% of base price
        # Heavy discounts reduce profit margin significantly
        cost_ratio = np.random.uniform(0.45, 0.62)
        unit_cost = unit_price * cost_ratio
        total_cost = quantity * unit_cost
        profit = round(total_sales - total_cost, 2)
        
        age = c_info['age']
        if age < 25:
            age_group = '18-24'
        elif age < 35:
            age_group = '25-34'
        elif age < 50:
            age_group = '35-49'
        elif age < 65:
            age_group = '50-64'
        else:
            age_group = '65+'
            
        region = np.random.choice(regions, p=region_weights)
        payment = np.random.choice(payment_methods, p=payment_weights)
        
        records.append({
            'Transaction_ID': trans_id,
            'Date': dt.strftime('%Y-%m-%d'),
            'Customer_ID': c_id,
            'Age': age,
            'Age_Group': age_group,
            'Gender': c_info['gender'],
            'Customer_Segment': c_info['segment'],
            'Product_Category': category,
            'Product_Subcategory': subcat,
            'Product_Name': prod_name,
            'Quantity': quantity,
            'Price_Per_Unit': unit_price,
            'Discount': discount,
            'Total_Sales': total_sales,
            'Profit': profit,
            'Region': region,
            'Payment_Method': payment
        })

    df = pd.DataFrame(records)
    
    # Introduce a tiny amount of realistic nulls in optional fields to test null checks
    # e.g., 10 missing Payment_Method entries
    null_indices = np.random.choice(df.index, size=12, replace=False)
    df.loc[null_indices, 'Payment_Method'] = np.nan
    
    return df

if __name__ == '__main__':
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(data_dir, exist_ok=True)
    csv_path = os.path.join(data_dir, 'retail_sales_data.csv')
    df = generate_retail_data(seed=2025, num_records=1650)
    df.to_csv(csv_path, index=False)
    print(f"Dataset successfully created at {csv_path} with {len(df)} rows and {len(df.columns)} columns.")
