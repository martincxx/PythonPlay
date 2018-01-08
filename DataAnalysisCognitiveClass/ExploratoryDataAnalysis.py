#exploratory Data Analysis EDA

#descriptive statistics

df.describe() #mean, std count, min, max, quantiles

#To summarize categorical data you may use value_counts method

drive_wheels_counts = df["drive-wheels"].values_counts()

drive_wheels.counts.rename(columns={"drive-wheels":"value_counts", inplace=True})
drive_wheels_counts.index.name="drive-wheels"


#Box plot shows median, upper and lower quartile
#example
import seaborn as sns
sns.boxplot(x="drive-wheels", y="prices", data=df)

#scatter plot show relation between two variables: predictor x, target y

from matplotlib import pyplot as plt
import numpy as np
import matplotlib

y = df["engine-size"]
x = df["price"]
plt.scatter(x, y)

#now, more details

plt.title("Scatterplot of Engine Size vs Price")
plt.xlabel("Engine Size")
plt.ylabel("Price")
