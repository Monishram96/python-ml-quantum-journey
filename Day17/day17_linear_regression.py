# IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split # split the dataset into training and testing part
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# LOADING DATA
df = pd.read_csv("../Day14/sales_dashboard_output.csv")

df=df[["Sales","Profit","Profit Margin %"]]
print(df.head())
print(df.describe())

# DEFINE FEATURES AND TARGET
X = df[["Sales"]].to_numpy()## Independent variable
y = df["Profit"].to_numpy()## Target variable

# SPLIT DATA
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
    )
print("Training sample:",len(X_train))
print("Testing samples:",len(X_test))

# TRAIN THE MODEL
model = LinearRegression()
model.fit(X_train,y_train)

print("Model Trained Successfully")

# EVALUATE THE MODEL
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(" Mean Squared Error:",round(mse,2))
print(" R^^ Score:",round(r2,3))
print("Slope(m):", model.coef_[0])
print("Intercept(c):",model.intercept_)

# PLOT PREDICTIONS
plt.scatter(X_test,y_test,color="blue",label="Actual")
plt.plot(X_test,y_pred,color="red",label="Predicted")
plt.title("Linear Regression: Sales Vs Profit")
plt.xlabel("Sales")
plt.ylabel("Pofit")
plt.legend()
plt.tight_layout()
plt.show()

# PREDICT CUSTOM VALUES
new_sales = np.array([[5000],[10000],[15000]])
predicted_profit = model.predict(new_sales)
print("\n Predicted Profit for new sales values:")
for sales, profit in zip(new_sales.flatten(),predicted_profit):
    print(f"Sales {sales}-> Expected Profit {profit:.2f}")
