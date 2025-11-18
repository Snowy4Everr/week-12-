# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# .append() - adds an item to the end of a list
# .extend() - adds multiple items to the end of the list 
# .pop() - removes and returns an item at a given index
# (default is the last item)
# .remove() - removes the first occurance of a specific value 
# .sort() - sorts the list in acsending order 
# .reverse() - reverses the order of the list

######################################################################################

#Why is a list more efficient than a variable ??????
# A list can hold multiple values while a variable can only hold one value at a time.


cakes = ["chocolate", "vanilla", "red velvet", "carrot"]
print(cakes)
# access the first item 
print(cakes[0])    
#access the last item 
print(cakes[-1])  
# want to chocolate cake instead of vanilla
cakes[0] = "strawberry"
print(cakes)       
# remove the last cake 
cakes.pop()
print(cakes)  
# insert a new cake  
cakes.insert(2, "funfetti")
print(cakes)

# Lists are part of the collections family in python. 

# Examples:


my_list = [1, 2, 3, 4, 5]
print(my_list)

print(len(my_list))
print(type(my_list))
print(my_list[0])
print(my_list[1:4])
print(my_list[1:])
print(my_list[:-1])
print(my_list[::-1])

my_list.append(6)
print(my_list)              #[1, 2, 3, 4, 5, 6]
my_list.extend([7, 8])
print(my_list)              #[1, 2, 3, 4, 5, 6, 7, 8]
my_list.extend([9, 10, 11])
print(my_list)              #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
my_list.pop(2)
print(my_list)              #[1, 3, 4, 5, 6, 7]
my_list.reverse()
print(my_list)              # [7, 6, 5, 4, 3, 2, 1]
my_list.reverse()
print(my_list)

new_list = list(range(12, 120))
print(new_list)
my_list.extend(new_list)
print(my_list)
num = list(range(120, 500))
my_list.extend(num)
print(my_list)
every_third_number = my_list[::3]
print(every_third_number)
every_tenth_number = my_list[::10]
print(every_tenth_number)
del my_list[::3]


my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

fav_food = ["pizza", "pasta", "tacos", "fries", "fruit"]

# Print the second and last item.

print(fav_food[1:])

# Add a new item using .append().

fav_food.append("garlic bread")
print(fav_food)

#Remove the first item using .pop(0).

fav_food.pop(1)
print(fav_food)

#Reverse your list using .reverse().

fav_food.reverse()
print(fav_food)
#Create a list of 3 lists (matrix), and access the middle element.

# sets = {1, 2, 3}

# sets are unoerdered collections of unique items 
# sets do not support indexing  or slicing 
# sets are mutable, meaning you can add or remove items 
# sets are created using curly braces {}
# do sets allow duplacate items? No, sets do not allow duplacate items

my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

my_set.add(6)
print(my_set)


# tuples are ordered collections of items 
# tuples are immutable, meaning you cannot modify them after creation
# tuples are created using parentheses ()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) 
print(type(my_tuple))