import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("../Day12/cleaned_sales_data.csv")
print(df)
# Plot Profit by Product (BAR)
df.groupby("Product")["Profit"].sum().plot(kind="bar",color="orange")
plt.title("Total Profit By Product")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.grid(True,linestyle="-",alpha=0.4)
plt.tight_layout()
plt.show()

df["Pofit Margin %"]=pd.to_numeric(df["Profit Margin %"],errors="coerce")
df=df.replace([np.inf,-np.inf],np.nan)
df=df.dropna(subset=["Profit Margin %"])
# Histogram of Profit Margins
plt.hist(df["Profit Margin %"], bins=5, color="purple", edgecolor="black")
plt.title("Distributiom of Profit Margin %")
plt.xlabel("Profit  Margin (%)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

#  Combines bar + line on same chart
fig,ax1=plt.subplots(figsize=(7,4))
df.groupby("Product")["Sales"].sum().plot(kind="bar",ax=ax1,color="lightgreen")
ax2=ax1.twinx()
df.groupby("Product")["Profit"].sum().plot(kind="line",ax=ax2,color="red",marker="o")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")
ax2.set_ylabel("Profit")
plt.title("Sales vs Profit by Product")
plt.tight_layout()
plt.show()
