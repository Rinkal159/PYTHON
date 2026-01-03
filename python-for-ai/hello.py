print("Hello world!") # single line print statement
print("""hii
im am rinkal""") # multi line print statement

#&------------------------------------------------------------------------------------------------------

# single line comment
"""
..
..
..
""" # multi line comment

#&------------------------------------------------------------------------------------------------------

# snake case is for variable declartion in python. eg. user_input, my_age, user_password
# camel case is for variable declartion in java. eg. userInput, myAge, userPassword

#&------------------------------------------------------------------------------------------------------

str = "rinkal" # single line string
str1 = """ hi
I 
Am
Rinkal
!!!
""" # Multi line string

#&------------------------------------------------------------------------------------------------------

#* String methods

#Strings in Python are immutable

print()
print('STRING METHODS')
print("--------------")

str = "I am Rinkal"
print(str * 5)
print(len(str))
print(str.startswith('i'))
print(str.endswith('al'))
print(str.upper())
print(str.lower())
print(str.title()) # title() capitalizes first character of each word
print(str.capitalize()) # capitalize() capitalizes only first character.

print()

#&------------------------------------------------------------------------------------------------------

# In python, divison always returns float.
simple_div = 10/3
floor_div = 10//3

#&------------------------------------------------------------------------------------------------------

# f-strings
name="Rinkal"
age=18
print(f"{name} is {age} years old.")
