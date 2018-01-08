
#importing CSV into Python
import pandas as pd
url="http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
#this assumes it has a header
df=pd.read_csv(url)
#To know name and type of values of columns (it could be object, int64, float64, datetime64, timedelta[ns])
types =(df.dtypes)
print (types)

#to obtain basic statistics, 
dt_stat=df.describe()
print ("Stat, using .describe")
print (dt_stat)
#initially it returns a dataframe of statistics of all numerical columns, but if you want to include all colums, you should do llike this
print ("Stat, using .describe include=all ")
df_all=df.describe(include="all")
print (df_all)
