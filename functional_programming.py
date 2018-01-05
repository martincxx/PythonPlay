
#lambda is keyword
#define a list with numbers from 0 to 15
my_list = range(16)

filter(lambda x: x % 3 == 0, my_list)

#filtering just python

languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x: x=="Python", languages)
#multiples of 3 or 5 between 1 and 15
threes_and_fives=[x for x in range(1,16) if x%3==0 or x%5==0]

##filtering using list and lambda
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message=filter(lambda x:x[::-2]!="X" , garbled)
print message
