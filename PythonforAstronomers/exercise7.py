"""
7. Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly
chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:
Output of the program (example):
Hello! What is your name?
Oak
Well, Oak, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Oak You guessed my number in 3 guesses!
"""
from sys import stdout
from random import randint
stdout.write("Lets play!\n")
x = input("Hello! What is your name?: ")

stdout.write("Well "+x+ ", I am thinking of a number between 1 and 20\n")
secret =randint(1, 20)
guess=0
time=1
while guess!=secret:
    guess = input("Take a guess: ")
    g=int(guess)
    if g==secret:
        stdout.write("Good job "+x+ "! You guessed my number in "+str(time)+ " guesses!\n")        
        break
    elif g<secret:
        stdout.write("Your guess is too low.\n")
    else:
        stdout.write("Your guess is too high.\n")
    time+=1
