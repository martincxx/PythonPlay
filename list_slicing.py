l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]


to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']

my_list = range(1, 11)

# reverse order of elements
backwards=my_list[::-1]

to_one_hundred = range(101)
# Striding each 10th element from right to left
backwards_by_tens=to_one_hundred[::-10]
print backwards_by_tens


#Create a list, to_21, that's just the numbers from 1 to 21, inclusive.
to_21=[i for i in range(1,22)]


#Create a second list, odds, that contains only the odd numbers in the to_21 list (1, 3, 5, and so on). Use list slicing for this one instead of a list comprehension.
odds=to_21[::2]
#Finally, create a third list, middle_third, that's equal to the middle third of to_21, from 8 to 14, inclusive.
middle_third=to_21[7:14:]
