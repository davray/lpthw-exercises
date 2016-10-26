numbers = []

def while_loop(start_value, max_value, interval):
    while start_value < max_value:
        print "At the top i is %d" % start_value
        numbers.append(start_value)

        start_value = start_value + interval
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % start_value

set_start = int(raw_input("Enter start value: "))
set_end = int(raw_input("Enter ending value: "))
set_interval = int(raw_input("Set interval: "))

while_loop(set_start, set_end, set_interval)

print "The numbers: "

for num in numbers:
    print num
