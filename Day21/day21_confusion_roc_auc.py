### IMPORTING THE FILES

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

### CREATING A DATA FRAME

data={
    "Hours_Study": [1,2,3,4,5,6,7,8,9,10],
    "Sleep_Hours": [8,7,7,6,6,5,5,4,4,3],
    "Pass":        [0,0,0,0,1,1,1,1,1,1]
    }
df = pd.DataFrame(data)
print(df)

### TRAIN/TEST SPLIT FORMATION

X = df[["Hours_Study","Sleep_Hours"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,random_state=42)

### TRAIN LOGITIC REGRESSION MODEL

model = LogisticRegression()
model.fit(X_train,y_train)

### PREDICTION & PROBABILITIES

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

### CONFUSION MATRIX PLOT

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, cmap="Blues", fmt = "d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

### AUC SCORE

auc = roc_auc_score(y_test,y_prob)
print("AUC Score:",auc)

### ROC CURVE PLOT

fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.figure(figsize = (6,5))
plt.plot(fpr, tpr, label=f"AUC = {auc:.2f}")
plt.plot([0,1],[0,1],linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
