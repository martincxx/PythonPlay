"""2. Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
	2.1. Use the module re (regular expressions)"""

def find_m(word):
    import re
    if re.match("[aeiou]$",word.lower()):
        return True
    else:
        return False

print find_m("A")
print find_m("x")
print find_m("0")
