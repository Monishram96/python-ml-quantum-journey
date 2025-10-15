import pandas as pd

data={
    'Name':['Alice','Bob','Charlie'],
    'M':[90,98,91],
    'S':[89,87,97],
    'E':[77,76,72]
    }
df=pd.DataFrame(data)

count_high=(df[['M','S','E']]>90).any(axis=1).sum()
print("Student Scoring > 90 in any subject:",count_high)

df['Average']=df[['M','S','E']].mean(axis=1)
df['Result']=df['Average'].apply(lambda x: 'Pass' if x>=40 else 'Fail')

df_sorted=df.sort_values(by='Average',ascending=False)
print('\nSorted DataFrame:\n',df_sorted)

df_sorted.to_csv("student_data.csv",index=False)
loaded_df=pd.read_csv("student_data.csv")
print("\nLoaded DataFrame form CSV:\n",loaded_df)
