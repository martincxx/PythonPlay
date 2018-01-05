def is_palindrome(word):
    backwards=word[::-1]
    if word==backwards:
        return True
    else:
        return False

#read from console
import sys
sys.stdout.write("Another way to do it!\n")
x = input("Word to examine: ")
y = is_palindrome(str(x))
sys.stdout.write(str(y))
