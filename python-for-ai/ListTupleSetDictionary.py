"""
    list: [] : square brackets
    tuple: () : parantheses
    set: {} : curly braces
"""

#* LIST
#* ____

list = ["rinkal", "mahi", 1, True, False]
list.remove(True)
print(list)

"""
    → List is same as "Array", but it can store "mix" data types.
    → "Ordered" collection of items.
    → "Mutable"
    → "Allows" duplicate values.
    
"""

print(list[-1]) #gives last element

list[len(list)-1] = False #Mutable

#* List methods
#* ______________

list.append("Priya")
list.pop() #if arguments are not passed, then pops last element, if argument passed then pops that index element.
list.insert(1, "None")
list.remove(True)
list.reverse()
list.sort()
list.copy()
list.extend(["dazai", "cutiepiee"])

#&----------------------------------------------------------------------------------------------------------

#* TUPLE
#* _____

tuple = ("rinkal", 1, True)

"""
    → Tuple is same as "List", but it is immutable.
    → "Ordered" collection of items.
    → "Allows" duplicate values.
"""

#* Tuple methods
#* _______________

# Tuple has only 2 methods because it is immutable

print(tuple.count(1))
print(tuple.index('rinkal'))
print(len(tuple))

#&----------------------------------------------------------------------------------------------------------

#* SET
#* ___

set = {1,2,3,3,4,"rinkal"}

"""
    → Set is same as "List", but it does not allow duplicate values.
    → "Unordered" collection of items.
    → "Mutable"
"""

print(set)
print(set[0]) #cannot access elements, throw an error

#* Set methods
#* ___________

set.add("mahi") #append element at last
set.remove(1) #element-based removing, not index-based


#* UNION, INTERSECTION, DIFFERENCE AND SYMMETRIC DIFFERENCE
#* ________________________________________________________

A = {1,2,3,4,5}
B = {3,5,6,7,8}

#* Union : |

# Will take both side's elements but does not take repeated elements two times, like if set A contains 2 and set B also contains 2, then it will take 2 only once.
print(A | B) 

#* Intersection : &

# Will take only values that are in both sets.
# Only takes common elements from both sides.
print(A & B)

#* Difference : -

# Will print those values that are not available in another set
# Elements in one set but not in another set.
print(A - B)
print(B - A)

#* Symmetric diffrenece : ^

# Will print values that are in either one set, not both, does not take repeated values.
print(A ^ B)

#&----------------------------------------------------------------------------------------------------------

#* DICTIONARY
#* __________

dictionary = {
    "name":"rinkal",
    "age":18,
    "degree":"bca"
}

"""
    → Dictionary is same as "object" in javascript, but here keys are also enclosed within double quotes.
    → Keys must be "unique"
    → "Mutable"
"""

# get value
print(dictionary["name"])
print(dictionary.get("name"))

# mutate value
dictionary["name"] = "rinkal"

# remove value
dictionary.pop("name")
del dictionary["name"]

# Dictionary methods
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

# loop on dictionary
for key, value in dictionary.items():
    print(f"key: {key}, value: {value}")