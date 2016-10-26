numbers = []

def while_loop(i, x):
    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


while_loop(0,6)

print "The numbers: "

for num in numbers:
    print num
