##COMPARE STANDARD SCALER  VS  MINMAX SCALER

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = {"A": [10,20,30,40,50], "B": [1,2,3,4,5]}
df = pd.DataFrame(data)
print("Orginal Data:\n", df)

# STANDARDSCALER
std = StandardScaler()
scaled_std = std.fit_transform(df)
print("\nStandardScaler:\n",scaled_std)

# MINMAXSCALER
mm = MinMaxScaler()
scaled_mm = mm.fit_transform(df)
print("\nMinMaxScaler:\n",scaled_mm)
