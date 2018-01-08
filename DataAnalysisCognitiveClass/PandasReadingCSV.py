#importing CSV into Python
import pandas as pd
url="http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
#this assumes it has a header
df=pd.read_csv(url)

#otherwise
df=pd.read_csv(url, header=None)

#show n first lines of df (a dataframe)
n=5
print ("First with head")
print (df.head(n))

#show n last lines of df (a dataframe)
print ("Then with tail")
print (df.tail(n))

#finally, save a copy to a csv file in local computer.
path ="~/Documents/Cognitive_Class/DataAnalysisPython/sample_data.csv"
df.to_csv(path)

"""
We can also work with hson, Excel, sql
with the following methods
pd.read_json()
pd.read_excel()
pd.read_sql()

Or exporting
df.to_json()
df.to_hdf()
df.to_sql()
"""
