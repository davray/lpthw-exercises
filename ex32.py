the_count  = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennsies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for i in the_count:
    print "This is count %d" % i

# same as above
for i in fruits:
    print "A fruit of type: %s" % i

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists. first start with an empty one
elements = range(0,6)

# then use the range function to do a 0 to 5 counts
#for i in range(0,8):
#    print "Adding %d to the list." % i
    # append is a function that lists understand
#    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

# Study Drills
# 1. Take a look at how you used range. Look up the range function to
#    understand it.
# 2. Could you have avoided that for-loop entirely on line 22 and just
#    assigned range(0,6) directly to elements?
#    - It printed out the same results since range is building a list.
# 3. Find the Python documentation on lists and read about them. What other
#    operations can you do to lists besides append?
