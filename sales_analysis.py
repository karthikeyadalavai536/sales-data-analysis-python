import pandas as pd
import matplotlib.pyplot as plt

# Create sample sales data
data = {
    "Product": ["Laptop", "Phone", "Tablet",
                "Laptop", "Phone"],
    "Sales": [1200, 800, 400, 1500, 900]
}

df = pd.DataFrame(data)

# Calculate total sales
total_sales = df["Sales"].sum()

print("Total Revenue:", total_sales)

# Calculate sales by product
product_sales = df.groupby("Product")["Sales"].sum()

print(product_sales)

# Create a chart
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
