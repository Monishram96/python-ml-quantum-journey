import pandas as pd
import matplotlib.pyplot as plt
import os

data={
    'Region':['North','South','East','West','North','South','East','West'],
    'Product':['A','B','C','D','E','F','G','H'],
    'Sales': [12000, 8000, 6000, 15000, 20000, 10000, 7000, 5000],
    'Profit': [3000, 1000, 500, 4000, 5000, 1500, 1200, 800]
    }
df=pd.DataFrame(data)

df['Profit_Margin'] = (df['Profit']/df['Sales'])*100
df['Performance']=df['Profit_Margin'].apply(lambda x: 'High' if x>20 else 'Low')

os.makedirs("Day13/charts",exist_ok=True)

plt.figure(figsize=(8,5))
plt.bar(df['Product'],df['Profit_Margin'],color='skyblue',edgecolor='black')
plt.title("Profit Margin (%) by Product")
plt.xlabel("Product")
plt.ylabel("Profit_Margin")
plt.grid(axis='y',linestyle="--",alpha=0.7)
plt.tight_layout()
plt.show()

profit_by_region=df.groupby('Region')['Profit'].sum()
plt.figure(figsize=(6,6))
plt.pie(profit_by_region,labels=profit_by_region.index,autopct='%1.1f%%', startangle=90)
plt.title("total Profit By Region")
plt.tight_layout()
plt.savefig("Day13/charts/profit_by_region.png")
plt.show()
plt.close()


plt.figure(figsize=(8,5))
plt.plot(df['Product'],df['Sales'],marker='o',label='Sales')
plt.plot(df['Product'],df['Profit'],marker='s',label='Profit')
plt.title("Sales vs Profit BY Product")
plt.xlabel("Product")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True,linestyle='--',alpha=0.7)
plt.tight_layout()
plt.savefig("Day13/charts/sales_vs_profit.png")
plt.show()
plt.close()


df.to_csv("sales_final.csv",index=False)

print("chart saved in Day13/chart/")
print(" Final data saved in sales_final.csv")
