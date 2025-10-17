import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Day12/cleaned_sales_data.csv")
print("Data loaded:\n",df.head())

# Bar Chart: Sales By Product
product_sales=df.groupby("Product")["Sales"].sum()
plt.figure(figsize=(5,5))
product_sales.plot(kind="bar",color="skyblue")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.tight_layout()
plt.show()


# Pie Chart: Sales Distributed By Region
region_sales=df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(5,5))
region_sales.plot(kind="pie",autopct="%1.1f%%",startangle=90)
plt.title("Sales Distribution By Region")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Line Chart
## Convert 'Date' to datetime
df["Date"]=pd.to_datetime(df["Date"])

# Line Chart: Sales Over Time
plt.figure(figsize=(7,4))
plt.plot(df["Date"],df["Sales"],marker="o",linestyle="-",color="green")
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()


# Scatter Plot: Sales VS Profit
plt.figure(figsize=(6,4))
plt.scatter(df["Sales"],df["Profit"],color="red")
plt.title("Sales VS Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True,linestyle="-",alpha=0.6)
plt.tight_layout()
plt.savefig("Sales_VS_Profit.png")
plt.show()









































































































































































































                                             







               
