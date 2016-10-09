# create function that requires two variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# print string with decimal format char using first var value
	print "You have %d cheeses!" % cheese_count
	# print string with decimal format char using second var value
	print "You have %d boxes of crackers!" % boxes_of_crackers
	# print string
	print "Man that's enough for a party!"
	# print string with new line escape sequence
	print "Get a blanket!\n"
	
# print string 
print "We can just give the numbers directly:"
# call function using the given amounts for variables
cheese_and_crackers(20,30)

# print string
print "OR. we can use variables from our script:"
# assign new variables amounts
amount_of_cheese = 10
amount_of_crackers = 50
# call function using new variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print string
print "We can even do math inside too:"
# call function using the sum of the formulas given as variables
cheese_and_crackers(10 + 20, 5 + 6)

# print string
print "And we can combine the two, variables and math:"
# call function using the sum of our formulas as variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Study Drills
# 1. Go back through the script and type a command above each line
#    explaining in English what it does.
#	 - Code commented.
# 2. Start at the bottom and read each line backward, saying all the
#    important characters.
# 3. Write at least one more function of your own design and run it
#    10 different ways.
#	 - File: ex19_sd3.py
