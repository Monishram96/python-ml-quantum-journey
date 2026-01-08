### IMPORT THE NESSASARY
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

### DATA LOAD
data = {
    "Hours_Study": [1,2,3,4,5,6,7,8,9,10],
    "Sleep_Hours": [8,7,7,6,6,5,5,4,4,3],
    "Pass":        [0,0,0,0,1,1,1,1,1,1]
    }
df = pd.DataFrame(data)
print(df)

### FEATHURES AND TARGET
X = df[["Hours_Study","Sleep_Hours"]]
y = df["Pass"]

### TRAIN/TEST/SPLIT
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3, random_state=42)

### TRAIN DECISION TREE MODEL
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train,y_train)

### PREDICTIONS & ACCURACY
y_pred = model.predict(X_test)

acc = accuracy_score(y_test,y_pred)
print("Accuracy:",acc)

### CONFUSION MATRIX
cm = confusion_matrix(y_test,y_pred)

plt.figure(figsize = (5,4))
sns.heatmap(cm, annot = True ,cmap ="Greens", fmt = "d")
plt.title("Decision Tree - Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

### VISUALIZE THE DECISION TREE
plt.figure(figsize=(14,8))
plot_tree(
    model,
    feature_names = X.columns,
    class_names = ["Fail","Pass"],
    filled = True
    )
plt.title("Decision Tree Visualization")
plt.show()
