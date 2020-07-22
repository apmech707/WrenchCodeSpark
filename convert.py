''' This is a program that converts common units for you.
This program runs in the console and has no GUI. Have fun!'''

from convert_dependencies import *

check_logged_file()
info() 
set_pass()


while True:
    
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
                    print(i)
    
    elif c.lower().strip() == 'reset':
        change_pass()

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
        del(password, check, flag, flag2, admin, a, b)
    elif c:
        if str(c.strip()) in choices_allowed:
            if len(str(c.strip())) == 1:
                convert(c.strip())
                continue
        elif str(c.strip()) not in choices_allowed or len(str(c.strip())) > 1:
            choice_error()
            continue
