"""5. Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using list comprehensions"""

#using for loop	
def words_lenghts(words):
    lenghts=[]
    for x in words:
        lenghts.append(len(x))
    return lenghts

print words_lenghts(["oak", "delmalo", "rules"])

#using list comprehension	
def words_lenghts_list(words):
    lenghts=[len(x) for x in words]
    return lenghts

print words_lenghts_list(["oak", "delmalo", "rules"])

#the third way is not described how to do it
