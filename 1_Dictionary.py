"""Exercise - 1"""
"""Apni Dictionary"""
"""Q. Create a dictionary and take input from the user and return the meaning of the word from the dictionary"""

"""SOLUTION"""
"""APNI DICTIONARY"""

d1 = {"Set":"Set is a collection of well defined object", "Python":"Python is a language that computer understands",
"Laptop":"Computer that can be carried easily", "PC":"Personal Computer", "Mobile":"A better version of telephone"}
word = input()
b = word.capitalize()
print(d1[word])
