
#* print statement

print("Hello world!") # single line print statement
print("""hii
im am rinkal""") # multi line print statement

#&------------------------------------------------------------------------------------------------------

#* Comments

# single line comment
"""
..
..
..
""" # multi line comment

#&------------------------------------------------------------------------------------------------------

#* variable declaration

# snake case is for variable declartion in python. eg. user_input, my_age, user_password
# camel case is for variable declartion in java. eg. userInput, myAge, userPassword

#&------------------------------------------------------------------------------------------------------

#* string

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
print(str.swapcase())
print(str.find("a")) # indexOf() in javascript, if word is not present it returns -1
print(str.index("a")) # same as find(), but if word is not present then it raises an error
print(str.count("I"))
print(str.strip())
print(str.replace("Rinkal", "Rinku"))

print()

#&------------------------------------------------------------------------------------------------------

#* divion in python

# In python, divison always returns float.

simple_div = 10/3
floor_div = 10//3

#&------------------------------------------------------------------------------------------------------

#* f-strings

name="Rinkal"
age=18
print(f"{name} is {age} years old.")

#&------------------------------------------------------------------------------------------------------

#* Logical operators

age = 20

if(age>18 and age>25):
    print("Logical and: Both are correct that's why statement is printed.")
    
if(age>18 or age>25):
    print("Logical or: Any one condition is satisfied that's why statement is printed.")
    
if(not age>30):
    print("Logical not: if opposite of condition is satisfied, that's why statement is printed")
    
#&------------------------------------------------------------------------------------------------------

#* if-elif-else

need_coffee = input("Wanna some coffee? : ")

if(need_coffee.lower()=="yes"):
    print("Absoulutly!! grab your favourite coffee.")
elif(need_coffee.lower()=="no"):
    print("Oh! That's fine.")
else:
    print("please say \"yes\" or \"no\"")   
