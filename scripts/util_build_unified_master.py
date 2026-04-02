import pandas as pd

# Load relational files with the new columns
orders = pd.read_csv("../data/food_orders_vast.csv")
customers = pd.read_csv("../data/customers_profile.csv")
restaurants = pd.read_csv("../data/restaurants_master.csv")
reviews = pd.read_csv("../data/customer_reviews.csv")

print("Merging RELATIONAL DATA into the EXPANDED UNIFIED MASTER...")

# 1. Merge Orders with Customers (Includes Platform, Age_Group)
master = orders.merge(customers, on='Customer_ID', how='left')

# 2. Merge with Restaurants (Includes Delivery_Zone)
master = master.merge(restaurants, on='Restaurant_ID', how='left')

# 3. Merge with Reviews
master = master.merge(reviews, on='Order_ID', how='left')
master['Review_Text'] = master['Review_Text'].fillna('No Feedback')

# 4. Feature Engineering
master['Order_Timestamp'] = pd.to_datetime(master['Order_Timestamp'])
master['Signup_Date'] = pd.to_datetime(master['Signup_Date'])
master['Days_Since_Signup'] = (master['Order_Timestamp'] - master['Signup_Date']).dt.days

# Export the Complete Raw Dataset
master.to_csv("../data/food_retention_master.csv", index=False)

print("Expanded Master Complete: '../data/food_retention_master.csv' (100k rows, 20+ columns).")
