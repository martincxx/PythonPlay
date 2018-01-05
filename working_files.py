my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10
#writing a file
f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

#read and write
my_file=open("output.txt","r+")


#opening and printing a file in python

my_file=open("output.txt", "r")

print my_file.read()
my_file.close()

my_file=open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

