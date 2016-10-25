import time
import os

start_over = '''
\nStart over. Good luck and may the odds, be ever in your favor.
'''

os.system('clear')

def invalid_crypt(invalid_number):
    print "Please enter a valid selection:"

def check_crypt1(verify_number1):
    if verify_number1 == "1" or verify_number1 == "2":
        print start_over
    elif verify_number1 == "3":
        print "\nFirst number unlocked. Good job."
        get_crypt2 = raw_input("\nPlease enter second number: ")
        check_crypt2(get_crypt2)
    else:
        print start_over


def check_crypt2(verify_number2):
    if verify_number2 == "1" or verify_number2 == "2":
        print start_over
    elif verify_number2 == "3":
        print "\nSecond number unlocked. Good Job. One more left."
        get_crypt3 = raw_input("\nPlease enter third number: ")
        check_crypt3(get_crypt3)
    else:
        print start_over


def check_crypt3(verify_number3):
    if verify_number3 == "2" or verify_number3 == "3":
        print start_over
    elif verify_number3 == "1":
        print "\nYou have successfully unlocked the safe. Congratulations.\n"
    else:
        print "So close. Start over." + start_over

print "You must unlock the safe."
print "There are 3 options on the keypad: 1 2 3"

time.sleep(1)

get_crypt1 = raw_input("\nEnter first number: ")
check_crypt1(get_crypt1)
