
#* Slicing
#* _______

# Slicing can be performed on 
       #*String, List, Tuple, and even on range.
       
# Cannot be performed on 
       #*set and dictionary.


#* On list:
list = [1,2,3,4,5,6,7,8,9,10]

print(list[1:5]) #1 to 4
print(list[5:]) #5 to all
print(list[:5]) #0 to 4

print(list[:]) #shallow copy
print(list[::-1]) #reverse a list

print(list[2::2]) #starting from 2, and step is 2, so 2 to all and jumping by 2

print(list[-5:]) #last 5 to all 
print(list[-5:-2]) #last 5 to last 2

print(list[:-2]) #0 to last 2

#operations
list[2:5] = [30, 40, 50] #modifying data
list[2:5]= [] #deleting data

