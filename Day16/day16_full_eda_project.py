# IMPORT AND LOAD DATA
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"]=(8,5)

df=pd.read_csv("../Day14/sales_dashboard_output.csv")

print(" Data loaded:",df.shape)
print(df.head())

# DATA CLEANING
print(df.info()) ###display the summary information about the dataframe
print(df.isnull().sum())  ###check how many missing(NaN) values are in each column

df.fillna({"Profit":0, "Sales":0},inplace=True)#handle missing values
df.drop_duplicates(inplace=True)#remove duplicates
df["Date"]=pd.to_datetime(df["Date"],errors="coerce")#convert data column to datatime
print("After cleaning:",df.shape)

# BASIC STATS
print(df.describe().T)  ### gives you summary statistics for all numeric columns
    # the T is used for the transpose> which helps to flips rows<->columns making the table easier to read vertically
##unique values
print("Regions:",df["Region"].unique()) ### list all distict region names in the dataset 
print("Top 5 products:",df["Product"].value_counts().head())

# UNIVARIATE ANALYSIS
sns.histplot(df["Sales"],bins=20,kde=True)
plt.title(" Sales Distribution")
plt.show()

sns.boxplot(x=df["Profit"])
plt.title("Profit outlier Check")
plt.show()

# BIVARIATE ANALYSIS
sns.scatterplot(x="Sales",y="Profit",hue="Region", data=df)
plt.title("Sales vs Prrofit by Region")
plt.show()

sns.barplot(x="Region",y="Profit", data=df, estimator=np.sum)
plt.title("Totle Profit by region")
plt.show()

# TIME SERIES VIEW
df["Month"]=df["Date"].dt.to_period("M").dt.to_timestamp()
monthly=df.groupby("Month")[["Sales","Profit"]].sum().reset_index()

sns.lineplot(x="Month",y="Sales",data=monthly,marker="o",label="Sales")
sns.lineplot(x="Month",y="Profit",data=monthly,marker="x",label="Profit")
plt.title(" Monthly Sales and Profit trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# CORRELATION + INSIGHTS
sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

print(" Insight: check which metric correlates most with Profit")


# SUMMARY + EXPORT
summary={
    "Total Sales":df["Sales"].sum(),
    "Total Profit":df["Profit"].sum(),
    "Avg Profit Margin":df["Profit Margin %"].mean(),
    "Top Region":df.groupby("Region")["Profit"].sum().idxmax(),
    "Top Product":df.groupby("Product")["Profit"].sum().idxmax()
}
summary_df=pd.DataFrame(list(summary.items()),columns=["Metric","Value"])
summary_df.to_csv("eda_summary.csv",index=False)
print(" Exported summary -> eda_summary.csv")















