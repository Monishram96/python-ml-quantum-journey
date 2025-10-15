import pandas as pd

# Load cleaned file
df=pd.read_csv("cleaned_sales_data.csv")
print("cleaned Sales data:\n",df)

# Total Scales and Profit
total_sales=df["Sales"].sum()
total_profit=df["Profit"].sum()
print("\nTotal Sales:\n",total_sales)
print("\nTotal Profit:\n",total_profit)

# Group by Product
product_summary=df.groupby("Product")[["Sales","Profit"]].sum()
print("\n Sales and Profit by Product:\n",product_summary)

# Group by region
region_summary=df.groupby("Region")["Sales"].sum()
print("\n Region summary:\n",region_summary)

# Top Performing Product
top_product=product_summary["Sales"].idxmax()
print("\n Top selling product:",top_product)

# Sort by Proft Margine
sorted_df=df.sort_values(by="Profit Margin %",ascending=False)
print("\nSorted by Profit Margine:\n",sorted_df)
