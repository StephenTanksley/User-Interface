# define a doubling functio nthat passes args by value
# function double(x){}
# const double = (x) => {}

def mult2(x):
    return x * 2

# define a doubling function for a list of variables passed by reference


def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2
    # return l


y = mult2(12)
print(y)

some_nums = [1, 2, 3, 4]
print(some_nums)
mult2_list(some_nums)
print(some_nums)
