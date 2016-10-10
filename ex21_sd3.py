# Study Drills
# 3. Once you have the formula worked out for the puzzle, get in there and see
#    what happens when you modify the parts of the functions. Try to change
#    it on purpose to make another value.

def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b
	
def subtract (a, b):
	print "Subtracting: %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "Multiplying: %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "Dividing: %d / %d" % (a, b)
	return a / b

def puzzle(a, h, w, i):
	print "\nHere's a puzzle."
	return add(age, subtract(height, multiply(weight, divide(iq, 2))))



print "\nLet's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)   

what = puzzle(age, height, weight, iq)
print "That becomes: ", what
