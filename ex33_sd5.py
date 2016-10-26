numbers = []

set_start = int(raw_input("Enter start value: "))
set_end = int(raw_input("Enter ending value: "))

for x in range(set_start, set_end):
        print "At the top i is %d" % x
        numbers.append(x)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % x


print "The numbers: "

for num in numbers:
    print num
