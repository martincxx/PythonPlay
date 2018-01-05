# dictionary example
dict = {"a":1, "e":2, "i":3,"o":4,"u":5,}    

#get keys and values as lists
capitals = [x.upper() for x in dict.keys()]
numbers=dict.values()


print capitals
print numbers

#now as tuples
print tuple(capitals)
print tuple(numbers)
