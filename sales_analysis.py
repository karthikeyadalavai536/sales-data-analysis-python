import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert order date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Display dataset
print("SALES DATA")
print(df.head())

# Total revenue
print("\nTotal Revenue:", df["Sales"].sum())

# Average sales
print("Average Sales:", df["Sales"].mean())

# Product-wise sales
product_sales = df.groupby("Product")["Sales"].sum()
print("\nProduct-wise Sales:")
print(product_sales)

# Region-wise sales
region_sales = df.groupby("Region")["Sales"].sum()
print("\nRegion-wise Sales:")
print(region_sales)

# Monthly sales
monthly_sales = df.groupby(
    df["Order_Date"].dt.to_period("M")
)["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Product sales chart
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Monthly sales chart
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
