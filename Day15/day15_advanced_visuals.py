# IMPORTING LIB
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("../day14/sales_dashboard_output.csv")

print(" Data Loaded:",df.shape)
print(df.head())

# SET A VISUALIZATION STYLE
sns.set_style("darkgrid")
plt.rcParams["figure.figsize"]=(8,5)
plt.rcParams["font.size"]=10

# CORRELATION HEATMAP
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True,cmap="coolwarm",fmt=".2f",linewidths=0.5)
plt.title(" Correlation Heatmap")
plt.show()

# PAIRPLOT
sns.pairplot(df,vars=["Sales","Profit","Profit Margin %"],hue="Region",diag_kind="kde")
plt.suptitle(" Pairplot: Region VS Sales,Profit,Margin",y=1.02)
plt.show()

# BAR PLOT
top5 = df.groupby("Product")["Profit"].sum().nlargest(5).reset_index()

sns.barplot(x="Profit",y="Product", data=top5,hue="Product",palette="magma",legend=False)
plt.title(" Top 5 Profitable Product")
plt.xlabel("Total Profit")
plt.ylabel("Product")
plt.show()

# BOX PLOT
sns.boxplot(x="Region",y="Profit",data=df,hue="Region",palette="Set2",legend=False)
plt.title(" Profit Distribution by Region")
plt.show()

# LINE CHART WITH STYLE
sns.lineplot(x="Date",y="Sales",data=df,marker="o",color="teal",label="Sales")
sns.lineplot(x="Date",y="Profit",data=df,marker="x",color="orange",label="Profit")

plt.title(" Sales & Profit Over Time(Styled)")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.legend()
plt.grid(alpha=0.4)
plt.tight_layout()
plt.show()

# ADD ANNOTATIONS
highest_sales= df["Sales"].max()
best_row=df[df["Sales"]== highest_sales].iloc[0]

plt.figure(figsize=(8,4))
sns.barplot(x="Product",y="Sales",data=df,hue="Product",palette="Blues_d")
plt.title(" Sales by Product(with Annotation)")

plt.text(
    x=list(df["Product"]).index(best_row["Product"]),
    y=highest_sales+10,
    s=f"Top {best_row['Product']}-> ${highest_sales}",
    color="red",
    fontweight="bold"
    )
plt.tight_layout()
plt.show()

plt.savefig("advanced_visuals_dashboard.png")
print(" Saved all Visuals as 'advanced_visuals_dashboard.png'")

























