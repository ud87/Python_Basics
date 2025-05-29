# Addition
added = 2 + 3
print(f"2 + 3 = {added} (should be 5)")

# Multiplication
multiplied = 2 * 3
print(f"2 * 3 = {multiplied} (should be 6)")


# == Subtraction ==
subtracted = 2 - 3
print(f"2 - 3 = {subtracted} (should be -1)")

# == Division ==
divided = 2 / 3
print(f"2 / 3 = {divided} (should be 0.6666666666666666)")

# This kind of 'decimal point' number, 0.6666666666666666 is called a float, by
# the way, meaning 'floating point'.


# == Modulus == Sometimes known as "remainder if we divide 3 by 2"
modulus = 3 % 2
print(f"3 % 2 = {modulus} (should be 1)")

# == Floor division == Sometimes known as "division without remainder"

floor_divided = 2 // 3
print(f"2 // 3 = {floor_divided} (should be 0)")

# == Exponentiation == Sometimes known as "2 to the power of 3"
expr = 2 ** 3
print(f"2 ** 3 = {expr} (should be 8)")


# The expression is the fundamental unit of computation in your program. It is
# the combination of data and operators (and some other things) to produce a
# result.

# Here are some more examples of expressions:

2            # Evaluates to: 2
2 + 3        # Evaluates to: 5
2 * 3        # Evaluates to: 6
2 + 3 * 4    # Evaluates to: 14
print(f"2 + 3 * 4 = {2 + 3 * 4}")

print(f"(2 + 3) * 4 = {(2 + 3) * 4}")



#=========================================================
#statement 

added = 2 + 3

# Is this a statement? Yes!
#
# That statement uses the `=` operator to assign the result of the expression on
# the right (`2 + 3`) to the name on the left (`added`).
#
# It's called a statement because it changes the 'state' of the program.
#
# What's the state of a program? Let's take a look at an example.
my_favourite_number = 99

print(f"My favourite number is: {my_favourite_number}")
print("---")


# == Exercise One ==

print("")
print("Function: divide_by_two_and_add_one")

def divide_by_two_and_add_one(num):
  # Divide num by two and add one to the result
  result = num / 2 + 1
  return result

check_that_these_are_equal(
  divide_by_two_and_add_one(6),
  4.0
)

# == Exercise Two ==

print("")
print("Function: multiply_by_forty_and_add_sixty")

def multiply_by_forty_and_add_sixty(num):
  # Multiply num by forty, and then add sixty
  result = num * 40 + 60
  return result

check_that_these_are_equal(
  multiply_by_forty_and_add_sixty(3423),
  136980
)

# == Exercise Three ==

print("")
print("Function: add_together_and_double")

def add_together_and_double(num_a, num_b):
  # Add together num_a and num_b, then double the result
  result = (num_a + num_b) * 2
  return result

check_that_these_are_equal(
  add_together_and_double(3, 4),
  14
)

