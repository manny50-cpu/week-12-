# Objective:
# Students will understand how to create, modify, and access elements in Python lists.
# append= add to list at the end of a list
# extend adds mutliple things to a list
# len = how long the thing is 
# type= identifies the class of thing
# extend= adds more than one thing to a list
# pop= removes something from a list and returns it at a given index
# pop() for last item
# reverse= reverses the order of things in a list
##############################################################
# #why is a list more useful than a variable?
# a list can hold multiple values
#  while a variable can only hold one value at a time
cakes = ['Chocolate','vanilla', 'red velvet', 'carrot']
print(cakes)
print(cakes[0])
print(cakes[-1])
cakes[0] = 'strawberry'
print(cakes)
cakes[1] = 'lemon'
print(cakes)
cakes.append('Fudge')
print(cakes)
cakes.pop()
print(cakes)
cakes.insert(2, 'funfetti')
print(cakes)



# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#lists are part of the collectios family in python
# creating a list
# Examples:
# my_list= [1,2,3,4,5]
# print(my_list)
# print(len(my_list))
# print(type(my_list))
# print(my_list[0])
# print(my_list[1:4])
# print(my_list[1:])
# print(my_list[:-1])
# print(my_list [::-1])

# my_list.append(6)
# print(my_list) #adds to my list
# my_list.extend([7,8])
# print(my_list)
# my_list.extend({8,9,10,11})
# print(my_list)
# my_list.pop()
# print(my_list)
# my_list.pop(2)
# print(my_list)
# my_list.reverse()
# print(my_list)
# my_list.remove(4)

# new_list =list(range(12,120))
# print(new_list)
# my_list.extend(new_list)
# print(my_list)
# new1_list = list(range(120,620))
# new_list.extend(new1_list)
# print(new1_list[: : 3])
# print(new1_list[::4])
# del new1_list[: : 3]
# print(new1_list)

# my_list = ['apple'
# , 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
food= ['ice cream', 'burger', 'pizza', 'cereal', 'rice krispies']
# Print the second and last item.
print(food[3:])
# Add a new item using .append().
food.append('lol')
print(food)
# Remove the first item using .pop(0).
food.pop(0)
print(food)
# Reverse your list using .reverse().
food.reverse()
print(food)
# Create a list of 3 lists (matrix), and access the middle element.
#sets = {1,2,3}
#sets are unordered collections of unique items 
# sets do not support indexing or slicing
# sets are mutable, meaning you can add or remove items
# sets are created using curly braces {}
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)
print( 4 in my_set) #true
print(3 in my_set) #false

# tuples are ordered collections of items
# tuples are immutable, meaning you cnanot modify them after creation
# typels are created using parentheses()
my_tuple = (1,2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1:4])

