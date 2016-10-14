# print string 
print "\nLet's practice everthing."
# print string with escape characters
print 'You\'d need to know \'bout escapes with \\ that do \nnewlines and \ttabs.'

# assign block of data to var poem
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# print some lines to help seperate block text
print "------------------------"
# print var poem data
print poem
print "------------------------"


# assign value of formula to var five
five = 10 - 2 + 3 - 6

# assign var five to string format character in print statement
print "This should be five: %s" % five

# create function requiring var
def secret_formula(started):
	# assign product of formula to jelly_beans
	jelly_beans = started * 500
	# assign quotient of formula to var jars
	jars = jelly_beans / 1000
	# assign quotient of formula to var crates
	crates = jars / 100
	# call return to store expression list value of variables
	return jelly_beans, jars, crates
	
# assign value to var 	
start_point = 10000
# give function secret_formula() new variable names
beans, jars, crates = secret_formula(start_point)

# print start_point value with decimal format character
print "With a starting point of: %d" % start_point
# print variables using format characters
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
# assign quotient formula to var
start_point = start_point / 10
# print string
print "We can also do that this way: "
# call function with start_point value then print function return list
print "We'd have %d beans, %d jars, and %d crates.\n" % secret_formula(start_point)

# Study Drills
# 1. Make sure to do your checks: read it backward, read it out loud, and put 
#    comments above confusing parts.
# 2. Break the file on purpose, then run it to see what kinds of errors you
#    get. Make you can fix it.
