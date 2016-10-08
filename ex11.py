print "How old are you? ",
age = raw_input()
print "How tall are you? ",
height = raw_input()
print "How much do you weigh? ",
weight = raw_input()

print "So, you're %s old, %s tall and you weigh %s." % (
    age, height, weight)
 
# Study Drills
# 1. Go online and find out what Python's raw_input does.
#	 - raw_input is a built in function that reads a string from standard
#    input. 
# 2. Can you find other ways to use it? Try some of the samples you find.
#	 - File: ex11_sd2.py 
# 3. Write another "form" like this to ask some other questions.
# 	 - File: ex11_sd3.py
# 4. Related to escape sequences, try to find out why the last line has
#    '6\'2"' with that \' sequence. See how the single-quote needs to be
#    escaped because otherwise it would end the string?
#	 - Changed the %r to %s to print the string instead of the raw value
