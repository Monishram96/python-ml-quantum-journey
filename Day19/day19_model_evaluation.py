# MODEL EVALUATION FEATURE SCALING
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# LOAD DATASET
data = {
    "Experience": [1,2,3,4,5,6,7,8],
    "TestScore": [60,70,75,80,85,88,90,95],
    "Salary": [35000, 40000, 50000, 55000, 60000, 65000, 70000, 75000]
    }
df = pd.DataFrame(data)
print(" Dataset:\n",df)

# SPLIT DATA
X = df[["Experience","TestScore"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state = 42)
print("\n Data Split Done")

# APPLY SCALING
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# TRAIN MODEL
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# PREDICT
y_pred = model.predict(X_test_scaled)

# EVALUATE
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test,y_pred)

print("\n Evaluation Result:")
print("Mean Squared Error:", round(mse,2))
print("R^2 Score:", round(r2,3))

                                    
