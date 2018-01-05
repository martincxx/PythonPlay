"""Exercises:
1. Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)"""

def max(x, y):
    if x!=y:
        if x>y:
            return x
        else:
            return y
    else:
        print ("Values %s, %s are equal")% (x, y)
        return 0
        

print max(0,1)

print max(2,1)

print max(1,1)
