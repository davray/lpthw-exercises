people = 20
cats = 30
dogs = 15


if people < cats:
	print "Too many cats! The world is doomed!"
	
if people > cats:
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	

dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."
	
if people and dogs:
	print "People are dogs."

# Study Drills
# 1. What do you think the if does to the code under it?
#	 - If the inequality is true then the if statement runs the code following
#	 the :. Else it skips over it.
# 2. Why does the code under the if need to be indented four spaces?
#	 - It lets the interpreter know that the block of indented code is to be
#	 ran with the code directly behind it.
# 3. What happens if it isn't indented?
#	 - The interpreter will return an error
# 4. Can you put other boolean expressions from Exercise 27 in the
#    if-statement? Try it.
