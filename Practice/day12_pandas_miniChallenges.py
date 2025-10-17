import pandas as pd

data={
    'Region':['North','South','East','West','North','South','East','West'],
    'Product':['A','B','C','D','E','F','G','H'],
    'Sales':[12000,8000,6000,15000,20000,10000,7000,5000],
    'Profit':[3000,1000,500,4000,5000,1500,1200,800]
    }
df=pd.DataFrame(data)
print("Initial DataFrane:\n",df)

# Region Lowest Total
region_sales=df.groupby('Region')['Sales'].sum()
lowest_region=region_sales.idxmin()
print("\nTotal sales by region:\n",region_sales)
print("\nRegion with lowest total sales:",lowest_region)

# Average Profit Margin
df['Profit_Margin']=(df['Profit']/df['Sales'])*100
avg_margin=df['Profit_Margin'].mean()
print("\nAverage Profit Margin:\n",avg_margin)

# Adding a Performance Columns
df['Performance']=df['Profit_Margin'].apply(lambda x: 'High' if x>20 else 'Low')
print("\nDataFrame with performance Column:\n",df)

# Saving a final CSV file
df.to_csv("sales_final",index=False)
print("\n Final result saved to sales_final.csv")
