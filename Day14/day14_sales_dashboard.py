#1 IMPORT THE LIB
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#2 DATA LOADING
df=pd.read_csv("../Day12/cleaned_sales_data.csv")

print("Data loaded successfully!")
print(df.head())

#3 CLEAN AND PREPARE
df.drop_duplicates(inplace=True) #drop duplication if any

df.fillna(0, inplace=True)# handle missing values

df["Sales"] =pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"]=pd.to_numeric(df["Profit"], errors="coerce")#ensure the numeric columns are clean

"""df["Profit Margin %"]= np.round((df["Profit"] / df["Sales"]) * 100, 2)# adding profit margine

print("Cleaned Profit Margine columns")
"""
df["Profit Margin %"]=np.where(
    df["Sales"] !=0,
    np.round((df["Profit"]/df["Sales"]) * 100,2),
    0
)
#4 SUMMARY STATS
print("\n BASIC SUMMARY STARTS:")
print(df.describe())

print("\n Total Sales:",df["Sales"].sum())
print("\n Total Profit:",df["Profit"].sum())
print("\n Average Profit Margine:",df["Profit Margin %"].mean())

#5 ANALYSIS 1:ALES BY PRODUCT
product_sales= df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\n Sales by Product:\n",product_sales)

##PLOT
plt.figure(figsize=(6,4))
product_sales.plot(kind="bar",color="teal")
plt.title("Total Sales By Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

#6 ANALYSIS 2: SALES BY REGION(pie)
region_sales= df.groupby("Region")["Sales"].sum()
plt.figure(figsize=(5,5))
region_sales.plot(kind="pie",autopct="%1.1f%%",startangle=90)
plt.title("Sales Distribution By Region")
plt.ylabel("")
plt.tight_layout()
plt.show()

#7 ANALYSIS 3: SALES TREND OVER TIME
df["Date"]=pd.to_datetime(df["Date"])

plt.figure(figsize=(8,4))
plt.plot(df["Date"],df["Sales"],color="orange",marker="o",label="Sales")
plt.plot(df["Date"],df["Profit"],color="green",marker="x",label="Profit")
plt.title("Sales & Profit Trend Date Time")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.legend()
plt.grid(True,linestyle="--",alpha=0.6)
plt.tight_layout()
plt.show()

#8 ANALYSIS 4: TOP 5 PROFITABLE PRODUCTS

top_profit=df.groupby("Product")["Profit"].sum().sort_values(ascending=False).head(5)
print("\n Top 5 Profitable Product:\n",top_profit)

##PLOT
plt.figure(figsize=(6,4))
top_profit.plot(kind="bar",color="gold")
plt.title("Top 5 Profitable Products")
plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.show()

df.to_csv("sales_dashboard_output.csv",index=False)
print("\n Final analyed data saved as sales_dashboard_output.csv")


















