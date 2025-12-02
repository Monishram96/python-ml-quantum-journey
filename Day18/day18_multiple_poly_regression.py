# IMPORT LIB
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# LOAD DATA
df=pd.read_csv("../Day14/sales_dashboard_output.csv")


data = df[[ "Sales" , "Profit" , "Profit Margin %" ]]
print("data loaded:",data.shape)
print(data.head())

# MULTIPLE LINEAR REGRESSION SETUP
X = data[["Sales","Profit Margin %"]].to_numpy()
y = data["Profit"].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)
print(" Model Trained Successfully!")

# EVALUATE MODEL
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Performance:")
print(" Mean Square Error :",round(mse,2))
print(" R2 score:",round(r2,3))
print(" Inertcept:",model.intercept_)
print(" Coefficients :", model.coef_)

# VISUALIZATION 2D
plt.figure(figsize=(6,4))
plt.scatter(y_test,y_pred,color="purple",alpha=0.6)
plt.xlabel("Actual Profit")
plt.ylabel("Predicted Profit")
plt.title(" Actual vs Predicted")
plt.grid(True)
plt.tight_layout()
plt.show()


# POLYNOMIAL REGRESSION
X_poly = data[["Sales"]].to_numpy()
y_poly = data["Profit"].to_numpy()

poly =  PolynomialFeatures(degree=2)
X_poly_transformed = poly.fit_transform(X_poly)

X_train, X_test, y_train, y_test = train_test_split( X_poly_transformed, y_poly, test_size=0.3, random_state=42)

poly_model= LinearRegression()
poly_model.fit(X_train,y_train)

y_pred_poly = poly_model.predict(X_test)

# EVALUTION POLYNOMIAL MODEL
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print(" \n Polynomial Regression Result:")
print("MSE:", round(mse_poly, 2))
print("R^2 Score:", round(r2_poly, 3))

# VISUALIZE POLYNOMIAL FIT
plt.scatter(X_poly, y_poly, color="blue" , alpha=0.5 , label= "Actual Data")

sorted_idx = np.argsort(X_poly.flatten())
plt.plot(
    X_poly.flatten()[sorted_idx],
    poly_model.predict(X_poly_transformed)[sorted_idx],
    color="red",
    linewidth=2,
    label="Polynomial Fit")

plt.title("Polynomial Regression Curve (Degree=2)")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.legend()
plt.tight_layout()
plt.show()











































