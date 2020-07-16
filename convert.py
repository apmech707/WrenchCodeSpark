''' This is a program that converts common units for you. Put all the files in the 
repository in one directory so that they can import correctly. Create a blank .txt file
and put it in the same directory. Name this file, logged_files.txt. This is the file that
the program will read and write your log to.This program runs in the console and has no GUI. Have fun '''

from convert_dependancies import value_error, choice_error, info, change_pass, set_pass, convert 

info() # This will display the list of option at the start of the program
set_pass() # This will check to see if it's the first time running the program and prompt to set a password if it is


while True: # this is the main while loop of the code
    
    choices_allowed = ('1', '2', '3', '4', '5', '6')
    c = input("Enter your choice of conversion:")
    print(f'\nYou entered: {c}')

    if c.lower().strip() == 'exit':
        quit()
    elif c.lower().strip() == 'help':
        info()  # This calls the function that lists the options
        continue
    elif c.lower().strip() == 'log':
        with open('logged_files.txt', 'r') as f:
            for line in f:
                for i in  line.split(","):
                    print(i) # prints out your log from the logged_files.txt
    
    elif c.lower().strip() == 'reset':
        change_pass() # calls the function imported from the dependencies to change password

    elif c.lower().strip() == 'clearlog':
        flag = True
        while flag:
            with open('new_program_flag.txt', 'r') as new_flag_file:
                password = new_flag_file.read()
            check = input("Enter your password!! Filthy Human!:\n")
            if check == password:
                print("Password accepted. Welcome developer")
                flag2 = True
                a = "y"
                b = "n"
                while flag2:
                    admin = input("Confirm delete log. Enter Y or N:\n")
                    if admin.lower().strip() == a:
                        with open('logged_files.txt', 'w')as f:
                            f.write("")
                            print("log deleted")
                            flag = False
                            flag2 = False
                    elif admin.lower().strip() == b:
                        print("log NOT deleted")
                        flag = False
                        flag2 = False
                    elif admin.lower().strip() != a and admin.lower().strip() != b:
                        continue
            elif check != password:
                print("NONSENSE!! HAVE YOU THE BRAIN WORMS?!!")
                continue
            elif check == 'exit':
                flag = False
    
    elif c:
        if str(c.strip()) in choices_allowed:
            if len(str(c.strip())) == 1:
                convert(c.strip())
                continue
        elif str(c.strip()) not in choices_allowed or len(str(c.strip())) > 1:
            choice_error()
            continue


