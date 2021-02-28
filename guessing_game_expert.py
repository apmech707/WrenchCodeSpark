"""
--EXPERT MODE--
(In this mode you get only 10 hints)

This is a game that generates a random number using the module random, then pipes that random number
into a function that lets you guess. While you're using it, please try and break it. I've tried to prevent
against it crashing, but if you find something that will break it, let me know. Also, it teaches you how to 
write really good code if you use your own software recklessly and try to get it to crash. Then by the time you
have designed against it and can't get it to crash, its most likely a pretty good code. Hope the comments are 
helpful for you. Have fun!"""

import random as woah
# https://docs.python.org/3/library/random.html

def guessing_game(answer):
    # def is how you create a function(or "define" a function) 
    # When I write guessing_game() further down in the code, it jumps back to here to run the function.
    # And whatever I write in the quotes when I call it, becomes assigned to the variable answer.
    
    flag = False
    count = 10
    
    while True:
        # https://stackoverflow.com/questions/3754620/what-does-while-true-mean-in-python

        if flag == False:
            print("Guess what number I am thinking of")
            flag = True
        elif flag: 
            # When you say "if" then some variable name, the condition you are testing is Boolean(True or False)
            # Asking " if flag", is asking if its True. You don't have to specify "== True" if you don't want to
            pass

        guess = input("\n")
        
        try:
            guess = int(guess)
        except ValueError:
            print("Enter a number to guess")
            continue
        # The try except block is useful when you anticipate that some code may throw an error
        # The code that may raise an exception goes in the try block. If it runs fine, then the except block is ignored(like an if-elif block)
        # If the exception that you write in occurs, though, the code in the try block stops bein executed and the except block runs.
        # This is handy becuase the program doesn't "crash", it just hadles the exception however you dictate it to in the except block.
        
        if guess == answer:
            print("You guessed it!")
            if count > 0:
                print(f"Congrats! You completed with {count} hints left over!")
                # f strings are a way to enter in a variable into a string and what prints will be the value of the variable.
                # The vairable has to be in those curly braces.
            elif count == 0:
                pass
            break
        
        elif guess != answer:
            print("\nThat's not it")
            flaggitha = False
            while count > 0:
                print(f"You have {count} hints left")
                if flaggitha == False:
                    print("Do you want to use one?")
                    flaggitha = True
                elif flaggitha:
                    pass
                
                do_ya = input()

                try:
                    do_ya = str(do_ya)
                except ValueError:
                    print("Enter yes or no.\n Do you want to use one of your hints?")
                    continue
                if do_ya.strip().lower() == "yes":
                    count -= 1
                    if  guess < answer:
                        print("Higher")
                        print("Guess again!")
                        break

                    elif guess > answer:
                        print("Lower")
                        print("Guess again!")
                        break
                
                elif do_ya.strip().lower() == "no":
                    print("Suit yourself. Guess again!")
                    break

                elif do_ya.strip().lower() != "yes" and do_ya.strip().lower() != "no":
                    print("Huh? I uhh.. don't know what that means. Try yes or no.")

guessing_game(woah.randint(0,200))

print("Would you like to play again?\n Type yes or no")
# A backslash in a string escapes what ever comes after it. You can add " without ending a string
# Or you can add \n which puts the next text on a new line
flaggy = False
while True:
    
    if flaggy == False:
        flaggy = True
    
    elif flaggy:
        print("Would you like to play again?\n Type yes or no")
        pass
    
    wouldya = input()

    if wouldya.strip().lower() == "yes":
        # The strip() method removes whitespace from the outsides of a string
        # I did this in case the the user accidentally adds a space when they input their response
        # The lower() method changes the string into all lowercase
        guessing_game(woah.randint(0,200))

    elif wouldya.strip().lower() == "no":
        print("Okay, Thanks for playing\nBye!")
        break
    elif wouldya.strip().lower() != "yes" and wouldya.strip().lower() != "no":
        print("I didn't understand, do you want to play again?")
        continue
