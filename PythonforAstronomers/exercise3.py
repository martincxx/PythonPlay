"""3. Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.	
	3.1. Use the module sys to run the program from the terminal getting the string as a parameter in the terminal."""
	
def is_palindrome(word):
    backwards=word[::-1]
    if word==backwards:
        return True
    else:
        return False

print is_palindrome("oak")
print is_palindrome("radar")
