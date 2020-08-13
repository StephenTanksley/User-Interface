# # # Print Hello World

# # print("Hello World!")

# # # Declare a variable

# # name = "Stephen"

# # # print a variable

# # print(name)

# # print("Hello" + name)

# # print(f"Hello, {name}.")

# # # Data structures

# # # Array - Lists and arrays are the same thing, just called different things.

# # p = [10, 20, 30, 50, 40]
# # print(p)
# # # add element to the end of p

# # p.append(60)
# # print(p)

# # p.sort()

# # # Let's loop over list P, and print every element.
# # # for every element in P, do some sort of code.

# # for element in p:
# #     print("Add 5 to elements: ", element + 5)

# # # print index and element at index of P
# # # p = [10, 20, 30, 50, 40] => enumerate(p) => [(0, 10), (1, 20), (2, 30)...}

# # for (index, element) in enumerate(p):
# #     print(f"Element at {index} is {p[index]}")


# # numbers = [1, 4, 9, 16, 25]

# # create a new list, of squares from the numbers list
# # this is the JavaScript-esque way of creating this list.
# # squares = []
# # for num in numbers:
# #     squares.append(num*num)

# # print(squares)

# # Let's use list comprehensions.
# # for each element from numbers, multiply by itself and add to cooler_squares
# # cooler_squares = [num ** 2 for num in numbers]
# # print(cooler_squares)


# # Let's create a list of just even numbers
# # evens = [num for num in numbers if num % 2 == 0]

# # create a new list containing names that start with S
# # names = ["Sarah", "Jorge", "sam", "Stephen", "Frank", "Bob", "shawn"]

# # s_names = [name.capitalize() for name in names if name[0].lower() == 's']
# # print(s_names)


# # s_names_verbose = []
# # for name in names:
# #     if(name[0].lower() == 's'):
# #         s_names_verbose.append(name.capitalize())

# # print("verbose: ", s_names_verbose)

# # Dictionaries! Otherwise known as maps/hashmaps/objects

# # a key -> value data structure.

# new_dict = {}

# food_dict = {
#     'apple': 'fruit',
#     'carrot': 'vegetable'
# }

# print(food_dict)

# food_dict['cucumber'] = 'vegetable'

# print(food_dict)

# # food_dict.apple is not allowed in python (only in JavaScript)

# chosen_food = 'apple'

# print(food_dict[chosen_food])


# # iterate through the keys and values of a dictionary
# # for element in dict, do some code

# for key, value in food_dict.items():
#     print(f'{key} : {value}')

# # .items() will give you keys and

# print('apple' in food_dict)
# print('carrot' in food_dict)


# # Tuples and Sets
# # What is a tuple? A collection of a couple of elements.

tup = (1, 2, 3, 4)
# # can't add things to it, can't remove things from it.

for item in tup:
    print(item)

# # access a particular element

# print(tup[1])

# # this lower line won't work.
# # tup[1] = "new thing"

# # Sets are basically dictionaries without values.

fruit = {'cucumber', 'apple', 'banana'}
fruit_array = ['cucumber', 'apple', 'banana']


for item in fruit:
    print(item)

if 'cucumber' in fruit:
    print("I don't think cucumber is a fruit.")


if 'cucumber' in fruit_array:
    print("I don't think cucumber is a fruit...and also use a set instead.")


#  a Set is unordered. If you want an ordered data structure, maybe use a List/Array instead. A Set is better for just checking to see if something exists or not.
