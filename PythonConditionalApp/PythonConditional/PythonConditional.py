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

