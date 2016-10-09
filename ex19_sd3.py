print "\nLet's do some math!\n"

def total_sum(figure_a, figure_b):
	print "a = %d" % figure_a
	print "b = %d" % figure_b
	print "Formula: %d + %d" % (figure_a, figure_b)
	outcome = figure_a + figure_b
	print "Outcome: %d\n" % outcome
	
print "First set: "
total_sum(1, 2)

print "Second set: "
first_number = 3
second_number = 4
total_sum(first_number, second_number)

print "Third set: "
first_number += 1
second_number += 2
total_sum(first_number, second_number)

print "Fourth set: "
total_sum(first_number * 2, second_number * 2)

print "Fifth set: "
total_sum(first_number + second_number, first_number * second_number)

new_first_number = int(raw_input("Enter first number for sixth set: "))
new_second_number = int(raw_input("Enter second number for sixth set: "))
total_sum(new_first_number, new_second_number)

print "Seveth set: "
total_sum(new_first_number + 1, new_second_number + 1)

print "Eight set: "
total_sum(new_first_number + first_number, new_second_number + second_number)

print "Ninth set: "
total_sum(1, 1)

print "Tenth set: "
final_number_one = first_number + new_first_number * 10
final_number_two = second_number + new_second_number * 10
total_sum(final_number_one, final_number_two)
