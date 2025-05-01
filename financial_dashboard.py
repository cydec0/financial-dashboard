import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Load data
df = pd.read_csv('data/sales_data.csv', parse_dates=['date'])

# Preprocess
df['month'] = df['date'].dt.to_period('M').astype(str)

# Total monthly revenue
monthly_revenue = df.groupby('month')['revenue'].sum()

# Revenue by product
product_revenue = df.groupby('product')['revenue'].sum().sort_values(ascending=False)

# Revenue by region
region_revenue = df.groupby('region')['revenue'].sum()

# Plot 1: Monthly Revenue Line Chart
plt.figure(figsize=(10, 5))
monthly_revenue.plot(marker='o')
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.tight_layout()
plt.savefig('output/monthly_revenue.png')
plt.close()

# Plot 2: Top 5 Products Bar Chart
top_products = product_revenue.head(5)
plt.figure(figsize=(8, 5))
top_products.plot(kind='bar', color='skyblue')
plt.title('Top 5 Products by Revenue')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output/top_products.png')
plt.close()

# Plot 3: Revenue by Region Pie Chart
plt.figure(figsize=(6, 6))
region_revenue.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Revenue by Region')
plt.ylabel('')
plt.tight_layout()
plt.savefig('output/revenue_by_region.png')
plt.close()

print("Dashboard generated! Check the 'output' folder for charts.")
