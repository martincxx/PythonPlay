"""6. Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome.
"""
def is_palindrome(word):
    backwards=word[::-1]
    if word==backwards:
        return True
    else:
        return False

#read from console
import sys
sys.stdout.write("Another way to do it!\n")
x = input("File to examine: ")


with open(x, "r") as my_file:
    data=my_file.readlines()

#print (data)
lines= [a.rstrip("\n") for a in data]
#print(lines)

for w in lines:
    if is_palindrome(w)==True:
        sys.stdout.write(str(w))
