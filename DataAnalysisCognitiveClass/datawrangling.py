
"""Pre-processing=data wrangling, data cleaning:
Objectives:
Handle missing values
format data
normalization (centering/scaling)
Data binning
Categorical values --- numerical values
"""


#first, ean example of adding 1 to all values of column symboling of our dataset
df["symboling"]=df["symboling"]+1


#missing values can be represented as a blank space, ?, 0, as N/A or as NaN

df.dropna() 
# axis = 0 drops entire row, 
# axis = 1 entire column 
# inplace = True #makes change efective on same df
#replace missing values with a value, in this case with the mean of that column

mean= df["normalized-losses"].mean()
df["normalized-losses"].replace(np.nan, mean)


#Data Formating. in this case we change result from mpg to l/100km
df["city-mpg"]=235/df["city-mpg"]

#rename column
#df.rename[columns={"old_name": "new_name"}, inplace=True]
df.rename[columns={"city_mpg": "city-L/100km"}, inplace=True]

#first check type of column using tail
df["price"].tail(5)
#convert type of column
df["price"]=df["price"].astype("int")

#DATA NORMALIZATION

#SIMPLE FEATURE SCALING  x_new = x_old/x_max

df["length"]=df["length"]/df["length"].max()

#MIN-MAX  x_new = (x_old - x_min)/(x_max - x_min) 

df["length"]=(df["length"] - df["length"].min())/(df["length"].max() - df["length"].min())

#Z-score   x_new = x_old-x.mean()/std_dev

df["length"]=df["length"]-df["length"].mean()/df["length"].std()
