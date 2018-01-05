# dictionary example
dict = {"a":1, "e":2, "i":3,"o":4,"u":5,}    

#function that obtains value from dictionary with a given key
def getSimpleValue(key):
    if key in dict.keys():
        return dict[key]
    else:
        return 0

#try correct instance
print getSimpleValue("a")

#otherwise
print getSimpleValue("x")

#another implementation of this 
def getSimpleValue2(key):
    if key in dict.keys():
        return dict.get(key)
    else:
        return 0
#try correct instance
print getSimpleValue2("a")

#otherwise
print getSimpleValue2("x")
