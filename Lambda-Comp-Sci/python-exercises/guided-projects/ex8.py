import time

# # function which prints every number from N to zero

# def print_num(n):

#     # This is the base case. The case where we stop running the function.
#     if n == 0:
#         print(n)
#         return

#     # recursive case - this is what takes us to the next sub-problem.
#     print_num(n-1)


# print_num(5)


# # def print_double(n):

# #     if n == 0:
# #         print(n)
# #         return

# #     print_double(n-1)
# #     print_double(n-1)
# #     return


# def fibonacci(n):

#     # base case

#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     # recursive case

#     result = fibonacci(n-1) + fibonacci(n-2)
#     return result


# print(fibonacci(100))

def partition(array):
    # this code breaks numbers into a left, pivot, and a right.
    left = []
    pivot = array[0]
    right = []

    # partition the numbers correctly into left and right arrays.
    for num in array[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return left, right, pivot


def quicksort(arr):
    # base case
    # what is the easiest array to sort?
    # "Conquer" step. <----
    if len(arr) <= 1:
        return arr

    # otherwise, divide.
    # Figure out how to properly split our data.
    left, pivot, right = partition(arr)
    # to make sure the pivot is a list of size 1.
    # pivot = [pivot]

    sorted_array = quicksort(left) + [pivot] + quicksort(right)
    return sorted_array


print(quicksort([5, 9, 3, 7, 2, 8, 1, 6]))
