#List: a data structure in Python that is a mutable, or changeable, ordered sequence of elements.

#List of string
fruits = ['apple', 'banana', 'cherry']

#List of ints
numbers = [1, 2, 3, 4, 5]

#List of hybrid values
hybrid = ['apple', 1, 2.5]

#Empty List
empty = []

#display list
#print(hybrid)

#Accessing List Elements
print(fruits[0])
print(fruits[1])
print(fruits[2])
#Reverse access
print(fruits[-0])
print(fruits[-1])
print(fruits[-2])

#Modifying a List
fruits[0] = 'orange'
print(fruits)

#Adding Elements
    #append() → Adds an item to the end
    #insert() → Adds an item at a specific index
fruits.append('grape')
print(fruits)
fruits.insert(1, 'mango')
print(fruits)

#Removing Elements
    #remove(value) → Removes the first occurrence of a value
    #pop(index) → Removes an item at an index (or last if no index is given)
    #clear() → Removes all elements
fruits.remove('banana')
print(fruits)
print(fruits.pop(1))
#before clear
print(hybrid)
#after clear
hybrid.clear()
print(hybrid)

#Looping Through a List
for fruit in fruits:
    print(fruit)

#List Length
print(len(fruits))

#Checking if an Item Exists
if 'apple' in fruits:
    print('Yes, apple is in fruits')
else:
    print('No, apple is not in fruits')

#Sorting a List
fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

