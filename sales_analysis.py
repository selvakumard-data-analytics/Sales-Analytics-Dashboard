import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("sales_data.csv")

# Total Sales
print("Total Sales =", df["Sales"].sum())

# Product-wise Sales
product_sales = df.groupby("Product")["Sales"].sum()

print("\nProduct Sales:")
print(product_sales)

# Best Selling Product
best_product = product_sales.idxmax()

print("\nBest Selling Product =", best_product)

# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Chart 1 - Product Sales
plt.figure()

product_sales.plot(kind="bar")

plt.title("Product Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()

# Chart 2 - Monthly Sales
plt.figure()

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()
category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory Sales:")
print(category_sales)

plt.figure()

category_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Category Sales Distribution")

plt.ylabel("")

plt.show()