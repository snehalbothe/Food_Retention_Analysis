import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Vibe Settings: 100,000 orders
np.random.seed(42)
n_orders = 100000
n_customers = 10000
n_restaurants = 500

print(f"Baking an EXPANDED retention dataset ({n_orders} orders)...")

# 1. Restaurants
res_ids = [f"RES-{1000 + i}" for i in range(n_restaurants)]
cuisines = ["Pizza", "Burger", "Indian", "Thai", "Healthy", "Sushi", "Dessert"]
# New Column: Zone Location
zones = ["Urban_Core", "Suburbs", "Industrial_Edge"]
res_df = pd.DataFrame({
    "Restaurant_ID": res_ids,
    "Cuisine": np.random.choice(cuisines, n_restaurants),
    "Delivery_Zone": np.random.choice(zones, n_restaurants),
    "Avg_Store_Rating": np.round(np.random.uniform(3.5, 4.9, n_restaurants), 1)
})

# 2. Customers
cust_ids = [f"CUST-{20000 + i}" for i in range(n_customers)]
start_date = datetime(2025, 1, 1)
signup_offsets = np.random.randint(0, 365, n_customers)
signup_dates = [start_date + timedelta(days=int(d)) for d in signup_offsets]
# New Column: Platform and Age Group
platforms = ["iOS", "Android", "Web"]
age_groups = ["Gen Z", "Millennial", "Gen X+"]
cust_df = pd.DataFrame({
    "Customer_ID": cust_ids,
    "Signup_Date": signup_dates,
    "App_Platform": np.random.choice(platforms, n_customers),
    "Age_Group": np.random.choice(age_groups, n_customers),
    "Is_Subscriber": np.random.random(n_customers) < 0.2
})

# 3. Orders (Vectorized)
order_indices = np.arange(n_orders)
order_ids = [f"ORD-{500000 + i}" for i in order_indices]
cust_samples = np.random.randint(0, n_customers, n_orders)
res_samples = np.random.randint(0, n_restaurants, n_orders)

dist_km = np.round(np.random.uniform(0.5, 12.0, n_orders), 1)
est_time = 15 + (dist_km * 3)

# New Environmental Factors: Weather & Traffic
weather = ["Sunny", "Rainy", "Stormy"]
traffic = ["Low", "Medium", "High"]
order_weather = np.random.choice(weather, n_orders, p=[0.7, 0.2, 0.1])
order_traffic = np.random.choice(traffic, n_orders, p=[0.5, 0.3, 0.2])

# Delay Logic including Environmental Factors
# Rain adds 10-15 mins, Stormy adds 30 mins
weather_delay = np.select([order_weather == "Rainy", order_weather == "Stormy"], [12, 30], default=0)
traffic_delay = np.select([order_traffic == "High", order_traffic == "Medium"], [15, 5], default=0)

delay_mask = np.random.random(n_orders) < 0.15
actual_delays = np.where(delay_mask, np.random.randint(20, 40, n_orders), np.random.randint(-5, 5, n_orders))
actual_time = np.round(est_time + actual_delays + weather_delay + traffic_delay, 1)

# New Behavioral Factors: Payment & Source
payments = ["Digital Wallet", "Credit Card", "Cash", "UPI"]
sources = ["Direct", "Search", "Social Ad", "Referral"]
order_payments = np.random.choice(payments, n_orders)
order_sources = np.random.choice(sources, n_orders)

# Sequence logic
sampled_signup_dates = cust_df.loc[cust_samples, "Signup_Date"].values
order_offsets = np.random.randint(0, 450, n_orders)
order_timestamps = [pd.to_datetime(d) + timedelta(days=int(o)) for d, o in zip(sampled_signup_dates, order_offsets)]

is_missing = np.random.random(n_orders) < 0.05
base_ratings = np.random.choice([5, 4, 3, 2, 1], n_orders, p=[0.4, 0.3, 0.15, 0.1, 0.05])
base_ratings = np.where(actual_time > 45, base_ratings - 1, base_ratings)
base_ratings = np.where(is_missing, base_ratings - 2, base_ratings)
final_ratings = np.clip(base_ratings, 1, 5)

order_df = pd.DataFrame({
    "Order_ID": order_ids,
    "Customer_ID": cust_df.loc[cust_samples, "Customer_ID"].values,
    "Restaurant_ID": res_df.loc[res_samples, "Restaurant_ID"].values,
    "Order_Timestamp": order_timestamps,
    "Distance_Km": dist_km,
    "Delivery_Time_Mins": actual_time,
    "Order_Total": np.round(np.random.uniform(15.0, 85.0, n_orders), 2),
    "Is_Missing_Item": is_missing,
    "Rating": final_ratings,
    "Weather": order_weather,
    "Traffic": order_traffic,
    "Payment_Method": order_payments,
    "Order_Source": order_sources
})

# 4. Review Generation
review_pool = {
    "Bad": ["Cold food", "Late delivery", "Wrong address", "Driver was lost", "Hungry and angry"],
    "Good": ["Perfect", "Delicious", "Fast delivery", "Hot and fresh", "Amazing packaging"]
}
review_mask = (final_ratings <= 2) | ((final_ratings == 5) & (np.random.random(n_orders) < 0.2))
reviews = [np.random.choice(review_pool["Bad"]) if r <= 2 else np.random.choice(review_pool["Good"]) for r in final_ratings[review_mask]]

review_df = pd.DataFrame({
    "Order_ID": np.array(order_ids)[review_mask],
    "Review_Text": reviews
})

# Save Everything
res_df.to_csv("../data/restaurants_master.csv", index=False)
cust_df.to_csv("../data/customers_profile.csv", index=False)
order_df.to_csv("../data/food_orders_vast.csv", index=False)
review_df.to_csv("../data/customer_reviews.csv", index=False)

print("Expanded Data Export Complete:")
print(f"- 13 Columns in 'food_orders_vast.csv'")
print(f"- {len(order_df)} Orders generated with Environmental Factors.")
