import pandas as pd

# Read CSV file
df=pd.read_csv("sales_data.csv")
print("Raw Data:\n",df)

# Basic info
print("\nShape:",df.shape)
print("\nColumns:",df.columns)
print("\nData type:\n",df.dtypes)

# Describe stats
print("\nStatistical Summary:\n",df.describe())

# Handle missing values
print("\nRows with missing data:\n",df[df.isna().any(axis=1)])

# Fill missing Sales with 0,Profit with mean
df["Sales"]=df["Sales"].fillna(0).apply(lambda x: round(x,2))
df["Profit"]=df["Profit"].fillna(df["Profit"].mean()).apply(lambda x: round(x,2))
print("\nAter filling missing values:\n",df)

# Filtering
high_sales=df[df["Sales"]>500]
print("\nHigh sales(>500):\n",high_sales)

# Add new calculated column
df["Profit Margin %"]=((df["Profit"]/df["Sales"])*100)
print("\nWith Profit Margin % column:\n",df)

# Save cleaned Data
df.to_csv("cleaned_sales_data.csv", index=False)
print("\n Cleaned data saved to cleaned_sales_data.csv")
