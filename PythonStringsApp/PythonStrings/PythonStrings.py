my_name = "Kay"
print(my_name)

# They are surrounded by double quotes:
my_name = "Kay"

# Or single quotes:
my_name = 'Kay'

# In Python, there's no meaningful difference between the two.
# Try out creating a string with your name in it:

your_name = "???"
print(your_name)

# == Exercise One ==

print("")
print("Function: get_first_letter")

def get_first_letter(the_str):
  # Return the first letter of the string
  return the_str[0]


# == Exercise Two ==

print("")
print("Function: get_last_letter")

def get_last_letter(the_str):
  # Return the last letter of the string
  return the_str[-1]

# == Exercise Three ==

print("")
print("Function: get_nth_letter")

def get_nth_letter(the_str, n):
  # Return the letter of the string at the specified index
  return the_str[n]


# == Exercise Four ==

print("")
print("Function: get_letters_between_four_and_eight")

def get_letters_between_four_and_eight(the_str):
  # Return the section of the string between indexes four and eight
  return the_str[4:8]



#we can find out length of string
name = "Hello"
print(f"Hello length is {len(name)} charactes long")
# note: len() is an independent function

#string functions
old_string = "Hello, YOUR_NAME"
new_string = old_string.replace("YOUR_NAME", "Uday")
print (new_string)

#note replace is method function

#convert to uppercase
def make_uppercase(string):
    return string.upper()

print(make_uppercase("hello"))


#convert to lowercase
def make_lowercase(word):
    return word.lower()

print(make_lowercase("FooT"))


#remove leading and trailing whitespace
def strip_whitespace(word):
    return word.strip()

print(strip_whitespace(" Harry   "))



#string concatenation
first_name = "udaya"
last_name = "rai"
print("My name is " + first_name + " " + last_name)

print(f"My name is {first_name} {last_name}")

