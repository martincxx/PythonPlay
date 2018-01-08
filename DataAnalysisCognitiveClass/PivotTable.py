import pandas as pd

import pandas as pd
#create a subset

df_test = df["drive-wheels", "body-style", "price"]
df_grp = df_test.group_by(["drive-wheels", "body-style"], as_index = False).mean()

df_pivot = df_grp.pivot (index = "drive-wheels", columns = "body-style" )
print (df_pivot)
