nums = [1,2,3,4,5,6,7,8,9]

# i want n for each n in nums
# my_list1 = []
# for n in nums:
#     my_list1.append(n)
# print(my_list1)

# -----------list comprehension--------
# my_list = [n for n in nums]
# print(my_list)

# i want n*n for each n in nums
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# -----------list comprehension--------
# my_list = [n*n for n in nums]
# print(my_list)

# map and lambda function

# In Python, the map() function is a built-in function that is used to apply a given function to each item in an iterable 
# (e.g., a list, tuple, or other iterable) and returns an iterator that yields the results. The map() function takes two or more arguments, 
# where the first argument is the function you want to apply, and
# the subsequent arguments are the iterables you want to apply the function to.

# map(function, iterable, ...)

# def square(n):
#     return n**2

iterate = [1,2,3,4,5]

# squared_numbers = map(square, iterate)
# list_squared_numbers = list(squared_numbers)
# print(list_squared_numbers)

#------lambda function------
#lambda arguments: expression
# lambda is the keyword used to define a lambda function.
# arguments are the input parameters, which can be zero or more.
# expression is a single expression that is evaluated and returned as the result of the lambda function.
# They are often used in conjunction with functions like map, filter, and sorted.

# add = lambda x, y: x + y
# result = add(3, 4)
# print(result)  # Output: 7

#---- lambda and map
# my_list = map(lambda n: n*n, iterate)
# print(my_list)
num = [1,2,3,4,5,6,7,8,9]
# my_list = []
# for num in num:
#     if num%2 == 0:
#         my_list.append(num)
# print(my_list)

# my_list = [n for n in num if n%2 == 0]
# print(my_list)

#------- filter function
# In Python, the filter() function is a built-in function used to filter elements from an iterable 
# (e.g., a list, tuple, or other iterable) based on a specified function or condition. It creates a 
# new iterable that contains only the elements for which the given function or condition returns True.
# filter(function, iterable)
# function: The function that determines whether an element is included in the filtered result. 
# This function should return True or False for each element in the iterable.
# iterable: The iterable (e.g., a list) from which elements are filtered.

# my_list = filter(lambda n: n%2 == 0, num)
# print(list(my_list))

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))

# print(my_list)
# my_list = [(num, letter) for letter in 'abcd' for num in range(4)]
# print(my_list)

names = ['bruce', 'clark', 'peter', 'logan', 'tony']
heros = ['hulk', 'superman', 'spiderman', 'wolverin', 'iron man']
zip_result = zip(names, heros)

my_dict = {}
for names, heros in zip(names, heros):
    my_dict[names] = heros
print(my_dict)

my_dict = {names: heros for names, heros in zip(names, heros)}
print(my_dict)

my_dict = {names: heros for names, heros in zip(names, heros) if names != 'peter'}
print(my_dict)
