# assign var string, giving format char value of 10
x = "There are %d types of people." % 10
# assign var string
binary = "binary"
# assign var string
do_not = "don't"
# assign var string, give format chars values from variables
y = "Those who know %s and those who %s." % (binary, do_not)
# print var
print x
# print var
print y
# print string with raw format char with value of var x
print "I said %r." % x
# print string with string format char with value of y
print "I also said: '%s'." % y
# assign var False
hilarious = False
# assign var with string that includes raw format char
joke_evaluation = "Isn't that joke so funny?: %r"
# print var values
print joke_evaluation % hilarious
# assign var with string
w = "This is the left side ..."
# assign var with string
e = "a string with a right side."
# print var w and var e
print w + e

# Study Drills
# 1. Go through this program and write a comment above each line
#    explaining it.
#	 - Coded commented.
# 2. Find all the places where a string is put inside a string. There
#    are four places.
#	 - Lines 8, 14, 16, 20.
# 3. Are you sure there are only four places? How do you know? Maybe
#    I like lying.
#    - Yes. Variables with numers are integers.
# 4. Explain why addding the two strings w and e with + makes a
#    longer string. 
#	 - We are adding var w and e together then printing them.
