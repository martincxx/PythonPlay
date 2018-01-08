#Grouping by df.Groupby()
import pandas as pd
#create a subset

df_test = df["drive-wheels", "body-style", "price"]
df_grp = df_test.group_by(["drive-wheels", "body-style"], as_index = False).mean()

print (df_group)
