#binning means dividing data of a column in a set of ranges as low, medium, high for price

#first calculate width of bin
bindwidth = int((max(df["price"])-min(df["price"]))/4)
bins = range(min(df["price"]), max(df["price"]), binwith)
group_names = ["low", "medium", "high"]

#finally, we create a column to display the bins for those data
import pandas as pd
df["price_binned"] = pd.cut(df["price"]), bins, labels=group_names)
