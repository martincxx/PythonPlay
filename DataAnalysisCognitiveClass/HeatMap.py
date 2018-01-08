
import pandas as pd
from matplotlib import pyplot as plt
#create a subset

df_test = df["drive-wheels", "body-style", "price"]
df_grp = df_test.group_by(["drive-wheels", "body-style"], as_index = False).mean()



df_pivot = df_grp.pivot (index = "drive-wheels", columns = "body-style" )
#create a heatmap

plt.pcolor(df_pivot, cmap="RdBBu")
plt.colorbar()
plt.show()
