import random as woah

def guessing_game(answer):
    
    flag = False
    
    while True:
        # https://stackoverflow.com/questions/3754620/what-does-while-true-mean-in-python

        if flag == False:
            print("Guess what number I am thinking of")
            flag = True
        elif flag: 
            # When you say "if" then some variable name, the condition you are testing is Boolean(True or False)
            # Asking " if flag", is asking if its True. You don't have to specify "== True" if you don't want to
            pass

        guess = input()
        
        try:
            guess = int(guess)
        except ValueError:
            print("Enter a number to guess")
            continue
        
        if guess == answer:
            print("You guessed it!")
            break

        elif guess != answer:
            print("That's not it")

            if  guess < answer:
                print("Higher")

            elif guess > answer:
                print("Lower")

guessing_game(woah.randint(-50,50))

print("Would you like to play again?\n Type yes or no")
# A backslash in a string escapes what ever comes after it. You can add " without ending a string
# Or you can add \n which puts it on a new line
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
        guessing_game(woah.randint(-50,50))

    elif wouldya.strip().lower() == "no":
        print("Okay, Thanks for playing\nBye!")
        break
    elif wouldya.strip().lower() != "yes" and wouldya.strip().lower() != "no":
        print("I didn't understand, do you want to play again?")
        continue
