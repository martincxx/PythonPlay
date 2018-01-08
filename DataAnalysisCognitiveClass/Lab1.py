# import pandas library
import pandas as pd
# read the online file by the URL provides above, and assign it to variable "df"
path="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(path,header=None)
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# replace headers
df.columns = headers

# recheck our data frame
df.head(10)
#obtain all records with not na price
df.dropna(subset=["price"], axis=0)

#obtain name of columns of df
col=df.columns
print(col

#save data from url to local
df.to_csv("automobile.csv")

# check the data type of data frame "df" by .dtypes
df.dtypes

# use .describe method to get the stat summary of "df"
df.describe()

# describe all the columns in "df" 
df.describe(include = "all")

# look at the info of "df" It provide a concise summary of your DataFrame.
df.info
