import pandas as pd

# Series
s = pd.Series([10,20,30,40,50]) 
print("Series:\n",s)
print("Values:",s.values)
print("Index:",s.index)

# Custome
marks=pd.Series([85,90,78,92],index=["Maths","Eng","Sci","CS"])
print("\nMarks Series:\n",marks)
print("CS marks:",marks["CS"])
print("Average Marks:",marks.mean())

# Create DataFrame
data={
    "Name":["Rahul","Priya","Moam","Sara"],
    "Age":[22,21,23,20],
    "Marks":[88,92,99,95]
    }
df=pd.DataFrame(data)
print("\nDataFame:\n",df)

# Access Columns and rows
print("\nName column:\n",df["Name"])
print("first row using iloc:\n",df.iloc[0])
print("Row with label(index):\n",df.loc[2])

# Add new columns
df["Grade"] = ["A","A+","O","A+"]
print("\nAfter adding Grade column:\n",df)

# Basic stats
print("\nMean marks:",df["Marks"].mean())
print("Max marks:", df["Marks"].max())

# Filtering
high_scorers=df[df["Marks"]>90]
high_scorers=high_scorers.sort_values(by="Marks",ascending=False)
print("\nStudent with > 90 marks:\n",high_scorers)
