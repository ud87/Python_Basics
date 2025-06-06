#dictionary is a key value pair

dialogue = {
    "actor1" : "Hey, are you ready ?",
    "actor2" : "I was born ready"
    }

print(dialogue["actor1"])
print(dialogue["actor2"])


text = "the quick brush jumped over the lazy crab"

# We'll use a dictionary to keep count of the letters we've seen. We'll start
# with an empty dictionary:

letter_counts = {}
# The keys will be the letters, and the values will be the number of that letter
# we've seen.

# We'll use a for loop to iterate over each letter in the string:

for letter in text:
  # We'll check if the letter is already in our dictionary of counts. We can do
  # this using the `not in` operator. 
  if letter not in letter_counts:
    # If it isn't, we'll add it to the dictionary with a starting count of 1.
    letter_counts[letter] = 1
    # Note that the syntax for assigning a value to a key in a dict is similar
    # to assigning a variable.
  else:
    # If it is, we'll increment the count for that letter.
    letter_counts[letter] = letter_counts[letter] + 1

# Let's print out the dictionary to see what we've got:
print(letter_counts)


# Write this function that counts the number of words by how many letters they
# have. For example:

# words:  ["hat", "cat", "I", "bird"]
# result: {3: 2, 1: 1, 4: 1}
# Since there are two words of length 3, etc.

def count_words_by_length(words):
  result = {}
  arr = words.split()  #convert words to list
  for word in arr:
      if len(word) not in result:
          result[len(word)] = 1
      else:
          result[len(word)] = result[len(word)] + 1
  return result

print(count_words_by_length("I am the guy who talks"))