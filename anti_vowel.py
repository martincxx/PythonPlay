def anti_vowel(text):
    anti=""
    i=0
    l=len(text)
    print (l)
    while(i<l):
        if(text[i].lower()!="a" and text[i].lower()!="e" and text[i].lower()!="i" and text[i].lower()!="o" and text[i].lower()!="u"):
            anti=anti+text[i]
        i=i+1
    return anti
##oak
print anti_vowel("Hello Python")  
