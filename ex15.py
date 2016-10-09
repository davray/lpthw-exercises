# import the function argv from module sys
from sys import argv
# give argv variables to unpack
script, filename = argv
# assign var txt to open var filename
txt = open(filename)
# print string with raw format char with var filename
print "\nHere's your file %r:" % filename
# print var txt contents open(file.read)
print txt.read()
txt.close()
# print string
print "Type the filename again:"
# get user input, assign user input to var file_again
file_again = raw_input("> ")
# open var filename, assign content to var txt_again
txt_again = open(filename)
# print txt_again contents using open(file.read)
print "\n" + txt_again.read()
txt_again.close()

# Study Drill
# 1. Above each line, write out in English what that line does.
#	 - Code commented.
# 2. If you are not sure, ask someone for help or search online. Many
#    times searching for "python THING" will find answers for what that
#    THING does in Python, Try searching for "python open."
# 3. I used the name "commands" here, but they are also called
#    "functions" and "methods." Search around online to see what other
#    people do to define these. Do not worry if they confuse you. It's 
#    normal for programmers to confuse you with vast extensive knowledge.
# 4. Get rid of the part from lines 10-15 where you use raw_input and
#    try the script then.
#	 - File: ex15_sd4.py
# 5. Use only raw_input and try the script that way. Think of why one way
#   of getting the filename would be better than another.
# 	- Depends on how interactive you want your script to be. You also 
#	 need to be careful with how raw_input assigns its value to a var
#	 as a string.
# 6. Run pydoc file and scroll down until you see the read() command
#    (method/function). See all the other ones you can use? Skip the
#    ones that have __ (two underscores) in front because those are 
#    junk. Try some of the other commands.
#	 - File: ex15_sd6.py
# 7. Start python again and use open from the prompt. Notice how you can
#    open files and run read on them right there?
# 8. Have your script also do a close() on the txt and txt_again
#    variables. It's important to close files when you are done with them
#	 = Added close() to Line 11 and Line 20 closing out files.
