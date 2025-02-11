'''
# tuple is immutable
# tuple is faster than list
# tuple is more memory efficient

A tuple in Python is an ordered, immutable collection of items.
It is similar to a list, but once a tuple is created, it cannot be modified (immutable).
Tuples are often used for fixed data structures.

When to Use Tuples Instead of Lists?
When you want data to remain constant (e.g., database records, settings).
When memory efficiency is important (tuples use less memory than lists).
When you need faster performance (tuples are faster than lists for iteration).
'''

#Creating a Tuple
numbers = (1,2,3,4,5)
fruits = ('apple','banana','cherry')
mixed = (1,'apple',3.4)
# Single element tuple (must have a trailing comma!)
single = (5,)

#Accessing Tuple Elements
print(fruits[1])
print(fruits[-1])

#To modify a tuple, you have to convert it to a list first.
fruits = list(fruits)
fruits[1] = 'orange'
fruits = tuple(fruits)
print(fruits)

#Concatenation (+)
numbers = numbers + (6,7,8)
print(numbers)

#Checking if an Item Exists
if 'apple' in fruits:
    print('Yes, apple is in fruits')
else:
    print('No, apple is not in fruits')

#Looping Through a Tuple
for fruit in fruits:
    print(fruit)

#Tuple Unpacking
person = ('John', 'Doe', 53)
name, surname, age = person
print(name)
print(surname)
print(age)

#Useful Tuple Methods
    #count(value) -> Counts occurrences of a value
    #index(value) -> Finds the index of a value
numbers = (1, 2, 3, 4, 2, 2, 5)
print("Appears: ", numbers.count(2))
print("@ Index: ", numbers.index(3))