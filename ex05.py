name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # centimeters
weight = 180 * 0.453592 # kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d kilograms." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
    
# Study Drills
# 1. Change all the variables so there isn't the  in front. Make sure
#    you change the name everywhere, not just where you used = to
#    set them.
#	 - Code changed.
# 2. Try more format characters. %r is a very useful one. It's like
#    saying "print this no matter what."
#	 - %r added to Line 17
# 3. Search onling for all the Python format characters.
#	 - %d, %i, %o, %u, %x, %X, %e, %E, %f, %F, %g, %G, %c, %r, %s, %
# 4. Try to write some variables that convert inches and pounds to
#    centimeters and kilos. Do not just type in the measurements.
#    Work out the math in Python.
#	 - Added conversion ammounts to Lines 3 and 4
