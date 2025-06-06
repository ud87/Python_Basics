#conditionals are used to execute something when a conditin is met
# if is a condition

name = "uday";
if name == "uday":
    print("Your name is uday")


leaves_on_the_tree = 0

if (leaves_on_the_tree == 0):
  print("It must be winter — or a dead tree")
else:
  print("This is a happy tree with nice leaves")


def is_first_of_the_month(day_number):
  # Return "First of the month!" if the day number is 1.
  if (day_number == 1):
      return "First of the month!"
  # Return "Not first of the month" otherwise.
  else:
    return "Not first of the month"


def has_five_chars(the_str):
  # Return "STRING is five characters long" if the string is five characters
  if (len(the_str) == 5):
      return f"{the_str} is five characters long"
  # Otherwise, return "Not five characters".
  else:
      return "Not five characters"


def a_is_less_than_b(a, b):
  # Uncomment this next line and replace ?? with the right operator
  return a < b


def a_is_greater_than_b(a, b):
  # return a ?? b
  return a > b

def a_is_less_than_or_equal_to_b(a, b):
  # return a ?? b
  return a <= b


def a_is_greater_than_or_equal_to_b(a, b):
  # return a ?? b
  return a >= b

def a_is_within_b(a, b):
  # return a ?? b
  return a in b


def not_a(a):
  # return ?? a
  return not a

def a_and_b(a, b):
  # return a ?? b
  return a and b


#while conditional 
i = 0
while i < 10:
    print(i)
    i = i + 1

# The `while` loop is like an `if`, in that it takes an expression that
# evaluates to True or False, and then executes its block of code if the
# condition is True.

# However, the `while` loop is different in that it keeps repeatedly executing
# the block for as long as the condition is True.

####################################################################
#Excercise
print("")
print("Function: add_cats_repeatedly")

# Write a function that adds the item "cats" to the given word_list, repeatedly,
# a number of times defined by the given count parameter.
# Example:
#    add_cats_repeatedly([], 3)
# => ['cats', 'cats', 'cats']

def add_cats_repeatedly(word_list, count):
  if (len(word_list) == 0):
      while len(word_list) < count:
        word_list.append("cats")
  else:
      while len(word_list) <= count:
        word_list.append("cats")
  return word_list

print(add_cats_repeatedly([], 2))

###################################################################w

#for loop
names = ["Harry", "Tom", "Sally"]

for name in names:
    print(f"Name: {name}")


for number in range(0, 10):
    print(f"Number: {number}")

# Summarising is processing down a list to a single value. It is sometimes also
# called 'reduce' — like reducing a broth to a thick soup.

# Add up all the numbers in the list
def add_up_numbers(numbers):
  result = 0
  for number in numbers:
    result = result + number
  return result

# Mapping is going through a list and converting ('mapping') each item to
# another item. This is useful when you want to perform the same operation
# across a list of items.

# Here's an example:

words = ['I', 'need', 'another', 'five', 'years']

first_letters = [] # This is our accumulator again

for word in words: # We go through each word
  first_letter = word[0] # Get the first letter
  # And append it to our accumulator list:
  first_letters.append(first_letter)

print(words)
print(first_letters)

# Return a new list of each number with 100 added
def add_one_hundred_to_numbers(numbers):
  result = []
  for number in numbers:
    result.append(number + 100)
  return result


# Filtering is going through a list and keeping only some of the items,
# typically according to a condition of some kind. This is useful when you only
# want to keep some of the items in your list.

# Imagine someone didn't put their age in
raw_ages = [32, 40, None, 1, 32]

clean_ages = [] # This is our accumulator again

for age in raw_ages: # We go through each age
  # We combine a for with an if to remove 'None' items
  if age != None:
    clean_ages.append(age)


# Return a new list with only the positive numbers
def only_positive_numbers(numbers):
  result = []
  for number in numbers:
    if number >= 0:
      result.append(number)
  return result
