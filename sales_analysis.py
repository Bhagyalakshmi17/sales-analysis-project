import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
df = pd.read_csv("../Data/sales_data_600_rows.csv")

# Step 2: Show first 5 rows
print("First 5 rows:")
print(df.head())

# Step 3: Show column names
print("\nColumn names:")
print(df.columns)

# Step 4: Check data types and missing values
print("\nData info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Step 5: Total sales and total profit
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)

# Step 6: Sales by category
sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(sales_by_category)

# Step 7: Profit by city
profit_by_city = df.groupby("City")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by City:")
print(profit_by_city)

# Step 8: Top selling products by quantity
top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("\nTop Selling Products:")
print(top_products)

# Step 9: Payment mode usage
payment_mode_count = df["Payment_Mode"].value_counts()
print("\nPayment Mode Count:")
print(payment_mode_count)

# Step 10: Convert date column to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Step 11: Create month column
df["Month"] = df["Order_Date"].dt.strftime("%b")

# Step 12: Monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()
print("\nMonthly Sales:")
print(monthly_sales)
# Save cleaned data to Excel ✅ ADD HERE
df.to_csv("../Excel/final_data.csv", index=False)

# -----------------------------
# Charts
# -----------------------------

# Chart 1: Sales by Category
sales_by_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Chart 2: Profit by City
profit_by_city.plot(kind="bar")
plt.title("Profit by City")
plt.xlabel("City")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 3: Top Selling Products
top_products.plot(kind="bar")
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

# Create Top 5 Products chart
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head()

top_products.plot(kind='bar', title="Top 5 Products by Sales")

plt.tight_layout()

# Save chart to charts folder
plt.savefig("../charts/top_products.png")

plt.show()

import matplotlib.pyplot as plt

# Chart 1: Sales by Category
sales_by_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("../charts/sales_by_category.png")
plt.show()

# Chart 2: Profit by City
profit_by_city.plot(kind="bar")
plt.title("Profit by City")
plt.xlabel("City")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../charts/profit_by_city.png")
plt.show()

# Chart 3: Top Selling Products
top_products.plot(kind="bar")
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../charts/top_products.png")
plt.show()