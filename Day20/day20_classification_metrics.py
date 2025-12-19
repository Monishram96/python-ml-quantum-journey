### IMPORTING THE NESSASARY
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score,f1_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
import pandas as pd

### CREATING THE SMALL DATA SET
data={
    "Hours_Study":[1,2,3,4,5,6,7,8,9,10],
    "Sleep_Hours":[8,7,7,6,6,5,5,4,4,3],
    "Pass":       [0,0,0,0,1,1,1,1,1,1]
    }

df = pd.DataFrame(data)
print(df)

### SPLIT DATA
X = df[["Hours_Study","Sleep_Hours"]]
y = df["Pass"]

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.3, random_state=42)

### TRAIN THE MODEL
model = LogisticRegression()
model.fit(X_train,y_train)


### PREDICTIONS
y_pred = model.predict(X_test)
print("Predictions:",y_pred)

### METRICS CALCULATION0
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

### print result
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("\nConfusion Matrix:\n", cm)
