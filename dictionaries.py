# Dictionaries in Python
# ========================
# Think of a Real Dictionary Book! 📖
# You know those big books with words and their meanings?
# Like:
#
# Cat → a furry animal that says meow 🐱
#
#
# Dog → a furry animal that says woof 🐶
#
#
# Sun → the big bright thing in the sky ☀️
#
#
# Every word has EXACTLY one meaning attached to it! 💛
# You look up the WORD...
# And you find its MEANING!
#
# Python Dictionary works EXACTLY the same way! 😊
# Instead of words and meanings...
# We call them KEYS and VALUES!
#
# EXPLANATION:
# ============
# A Python dictionary is a collection of key-value pairs.
# - KEYS: Like words in a real dictionary (unique identifiers)
# - VALUES: Like meanings/definitions (data associated with each key)
#
# Example:
# my_dict = {"Cat": "a furry animal that says meow 🐱",
#            "Dog": "a furry animal that says woof 🐶",
#            "Sun": "the big bright thing in the sky ☀️"}
#
# To access a value, you use the key:
# my_dict["Cat"]  # Returns: "a furry animal that says meow 🐱"
#
# Key features of dictionaries:
# 1. Unordered (in older Python versions) - ordered in Python 3.7+
# 2. Mutable - you can add, remove, or change key-value pairs
# 3. Keys must be unique - each key appears only once
# 4. Keys must be immutable - strings, numbers, tuples (not lists or dicts)
# 5. Values can be any data type - strings, numbers, lists, other dicts, etc.

my_dictionary = {
    "cat" : "a furry animal that says meow",
    "dog" : "a furry animal that says woof",
    "sun" : "the big bright thing in the sky"
}
print(my_dictionary["cat"])  # Output: a furry animal that says meow
print(my_dictionary["dog"])  # Output: a furry animal that says woof
print(my_dictionary["sun"])  # Output: the big bright thing in the sky

# Note:
# if the key is a string, you have to specify it as a string;
# keys are case-sensitive: 'Suzy' is something different from 'suzy'.
# And now the most important news: you mustn't use a non-existent key. 
# Trying something like this would cause an error:
# print(phone_numbers['president'])

# Fortunately, there's a simple way to avoid such a situation. 
# The 'in' operator, together with its companion 'not in', can salvage this situation.

# The following code safely searches for some French words:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

# Note:
# When you write a big or lengthy expression, it may be a good idea to keep it 
# vertically aligned. This is how you can make your code more readable and more 
# programmer-friendly, e.g.:

# Example 1:
dictionary = {
    "cat": "chat",
    "dog": "chien",
    "horse": "cheval"
}

# Example 2:
phone_numbers = {'boss': 5551234567,
                 'Suzy': 22657854310}

# This kind of formatting is called a hanging indent.

