import pandas as pd

# Create DataFrame form lists
student={
    "Name":["A","B","C","D"],
    "Maths":[80,95,67,89],
    "Science":[78,90,92,79],
    "English":[96,89,86,56]
    }
df=pd.DataFrame(student)
print("Student marks:\n",df)

# Calculate average marks from each student
df["Average"]=df[["Maths","Science","English"]].mean(axis=1).apply(lambda x: round(x,2))
print("\nAfter adding the Average:\n",df)

# Filter student with average > 85
top_students= df[df["Average"] > 85]
print("\top student(>85):\n",top_students)

# Find subject wise mean
print("\nSuject wise mean:\n",df[["Maths","Science","English"]].mean())

# Save Dataframe to csv
df.to_csv("student_data.csv",index=False)
print("\nCSV file saved successfully")
