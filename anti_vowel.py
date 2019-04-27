def anti_vowel(text):
    # Created vowels as a iterable list to shorten if clause #
    anti = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    # prints length directly instead of creating variable since it isn't reused in the code
    print (len(text))
    # changes the loop from a while loop to one that directly iterates over the characters instead of using an index
    for char in text:
        if(char.lower() not in vowels):
            anti += letter # uses += instead of 'anti = anti + letter' for some syntactic sugar
    return anti
##oak
print anti_vowel("Hello Python")  
