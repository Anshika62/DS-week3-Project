#Analyze a Simple Sales Dataset to find: total sales, best-selling product, and create a basic report
import pandas as pd
df = pd.read_csv("sales_data.csv")
print("---- BASIC INFO ----")
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print()

# Data Cleaning
# Check missing values
print("Missing Values Before Cleaning:")
print(df.isnull().sum())
print()

# Fill missing numeric values with 0
num_cols = df.select_dtypes(include=['int64','float64']).columns
df[num_cols] = df[num_cols].fillna(0)

# Fill missing string values with 'Unknown'
str_cols = df.select_dtypes(include=['object']).columns
df[str_cols] = df[str_cols].fillna("Unknown")

# Remove duplicates
df = df.drop_duplicates()
print("Missing Values After Cleaning:")
print(df.isnull().sum())
print()


# Sales Analysis
# Total sales

total_sales = df["Total_Sales"].sum()

# Best-selling product (by revenue)
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
best_product_sales = df.groupby("Product")["Total_Sales"].sum().max()

# Total quantity sold
total_quantity = df["Quantity"].sum()

# Region-wise revenue
region_sales = df.groupby("Region")["Total_Sales"].sum()

# 5. Generate Report

print("---- SALES ANALYSIS REPORT ----")
print(f"Total Revenue Generated: ₹{total_sales:,.2f}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Best Selling Product: {best_product} (₹{best_product_sales:,.2f})")
print("\n---- Revenue by Region ----")
print(region_sales)



