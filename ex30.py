# add value 30 to var people
people = 30
# add value 40 to var cars
cars = 40
# add value 15 to var trucks
trucks = 15

# evaluate inequality
if cars > people:
	# if true print string
	print "We should take the cars."
# if first expression is false try this one
elif cars < people:
	# print string if true
	print "We should not take the cars."
# if all expressions false then run this code	
else:
	# print string
	print "We can't decide."
	
if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."
	
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."
	
# Study Drills
# 1. Try to guess what elif and else are doing.
#	 - elif and else are giving more options to the if statement.
# 2. Change the numbers of cars, people, and trucks and then trace through
#    each if-statement to see what will be printed.
# 3. Try some more complex boolean expressions like cars > people.
# 4. Above each line write an English description of what the line does.
