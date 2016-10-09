# Study Drills
# 2. Write a script similar to the last exercise that uses read and 
#    argv to read the file you just created.
# Description:
#	This is a mock license/credential type file.

# import function argv from module sys
from sys import argv

# give argv some variables to unpack
script, user_name, user_pass, target_game = argv

# print string, print var with string format character
print '''
\nHello, %s! I appreciate you using this quick litle script!
''' % user_name 

print "-" * 25

# open var target_game, give write flag, store in var user_credits
user_credits = open(target_game, 'w')

# print disclosure, assign target_game to string format char
print '''

Please wait while I locate your credentials for %s

Credentials located!

CAUTION: All contents will be deleted. If you wish to cancel please press CTRL-C (^C) now.
If you would like to proceed press RETURN.
''' % target_game

# wait for user response using empty raw_input
raw_input('')
# print string
print "Writing data to file..."

# write user given data to file
user_credits.write("user_name: " + user_name)
user_credits.write("\n")
user_credits.write("password: " + user_pass)
# print string
print "\nClosing file. Ciao!"
# close file
user_credits.close()


