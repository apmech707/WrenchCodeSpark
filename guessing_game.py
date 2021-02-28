"""This is a game that generates a random number using the module random, then pipes that random number
into a function that lets you guess. While you're using it, please try and break it. I've tried to prevent
against it crashing, but if you find something that will break it, let me know. Also, it teaches you how to 
write really good code if you use your own software recklessly and try to get it to crash. Then by the time you
have designed against it and can't get it to crash, its most likely a pretty good code. Hope the comments are 
helpful for you. Have fun!"""

import random as woah
# https://docs.python.org/3/library/random.html

def guessing_game(answer):
    # def is how you create a function( or "define" an function)
    # When I write guessing_game() further down in the code, it jumps back to here to run the function.
    # And whatever I write in the quotes when I call it, becomes assigned to the variable answer.
    
    flag = False
    
    while True:
        # https://stackoverflow.com/questions/3754620/what-does-while-true-mean-in-python

        if flag == False:
            print("Guess what number I am thinking of")
            flag = True
        elif flag: 
            # When you say "if" then some variable name, the condition you are testing is Boolean(True or False)
            # Asking "elif flag", is asking if its True. You don't have to specify "== True" if you don't want to
            pass

        guess = input("\n")
        
        try:
            guess = int(guess)
        except ValueError:
            print("Enter a number to guess")
            continue
        # The try except block is useful when you anticipate that some code may throw an error
        # The code that may raise an exception goes in the try block. If it runs fine, then the except block is ignored(like an if-elif block)
        # If the exception that you wirte in occurs, though, the code in the try block stops bein executed and the except block runs.
        # This is handy becuase the program doesn't "crash", it just hadles the exception however you dictate it to in the except block.
        
        if guess == answer:
            print("You guessed it!")
            break
            # The break statement breaks you out of the while loop and you move on with the code below it.

        elif guess != answer:
            print("\nThat's not it")

            if  guess < answer:
                print("Higher")

            elif guess > answer:
                print("Lower")

guessing_game(woah.randint(-50,50))

print("Would you like to play again?\n Type yes or no")
# A backslash in a string escapes what ever comes after it. You can add " without ending a string
# Or you can add \n which puts the next text on a new line
flaggy = False
while True:
    
    if flaggy == False:
        flaggy = True
    
    elif flaggy:
        print("Would you like to play again?\n Type yes or no")
    
    wouldya = input()

    if wouldya.strip().lower() == "yes":
        # The strip() method removes whitespace from the outsides of a string
        # I did this in case the the user accidentally adds a space when they input their response
        # The lower() method changes the string into all lowercase
        guessing_game(woah.randint(-50,50))

    elif wouldya.strip().lower() == "no":
        print("Okay, Thanks for playing\nBye!")
        break
    elif wouldya.strip().lower() != "yes" and wouldya.strip().lower() != "no":
        print("I didn't understand, do you want to play again?")
        continue
        # Continue causes the while loop to halt and you jump back to top of the while loop where it continues.