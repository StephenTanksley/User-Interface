from itertools import product
import random
import functools
import time


def fibonacci(n):
    # base case
    if (n == 0):
        return 0
    if (n == 1):
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

# memoized - cache the results of your function calls.
# {
#   input_to_function: result_given_that_input
    # 1: mem_fibonacci(1) == 1
    # 2: mem_fibonacci(2) == 1
    # 3: mem_fibonacci(3) == 2

# }


def mem_fibonacci(n, cache):
    # base case
    if (n == 0):
        cache[0] = 0
        return 0
    if (n == 1):
        cache[1] = 1
        return 1

    # I want to get the answer for Fibonacci at n-1.
    # Let me check if I already have that value in my cache.
    if n in cache:
        return cache[n]

    # Otherwise...we run these two recursive calls.
    result_n_1 = mem_fibonacci(n-1, cache)
    result_n_2 = mem_fibonacci(n-2, cache)

    # ...and then save the result of EVERYTHING to the cache.
    result_at_n = result_n_1 + result_n_2

    # Then we
    cache[n] = result_at_n
    return result_at_n


# Tabulation example, start from 0 and go UP to N
# Keep track of what you've done already in a table going up to N.
def tab_fibonacci(n):
    # start at n=0 and n=1
    solution_table = [0 for _ in range(0, n+1)]
    solution_table[0] = 0
    solution_table[1] = 1

    for i in range(2, n+1):
        solution_table[i] = solution_table[i-1] + solution_table[i-2]

    return solution_table[n]


print(f'Tab fib: {tab_fibonacci(90)}')

start = time.time()
print(f'{mem_fibonacci(5, {})}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds.')
print(f'\n--------------------------------\n')

start = time.time()
print(f'{fibonacci(5)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds.')
print(f'\n--------------------------------\n')


def naive_scavenging(field):
    # generate all possible moves
    all_move_combos = list(product(['se', 'e', 'ne'], repeat=len(field) - 1))

    # for each combo of moves, try to traverse, and calculate the total gold collected
    for move_combo in all_move_combos:
        # start at the top left corner
        total_gold = field[0][0]
        col = 0
        row = 0
        for direction in move_combo:
            if direction == 'se':
                # try to move in the southeast direction
                if row > len(field) - 1:
                    break
                else:
                    row += 1
            elif direction == 'ne':
                # try to move in the northeast direction
                if row <= 0:
                    break
                else:
                    row -= 1
            # always move east after moving either south or north
            col += 1

            # total gold will be equal to the gold we grabbed using this move combo
            total_gold += field[row][col]

        if total_gold > max_gold:
            max_gold = total_gold
            output = f'{max_gold} can be acquired if we move {move_combo}'

    return output


def dp_scavenging(field):
    '''
    This function utilizes dynamic programming to reduce the number of duplicate calculations that are performed (compared to the naive approach). After a coordinate is visited, we save both i) the max amount of gold that can be picked up from that coordinate and ii) the path you'd have to travel to pick up maximum gold from that point. 

    Subpaths on the eastern side of the field that we visited multiple times in the naive approach are only visited once using dynamic programming.

    '''

    gold_cache = [[0 for _ in range(len(field))] for _ in range(len(field))]

    for col in range(len(field) - 1, -1, -1):
        for row in range(len(field)):
            # take all possible directions, and figure out max gold per direction
            east_gold = 0
            ne_gold = 0
            se_gold = 0

            # gold collected if we choose to go EAST
            if (col != len(field) - 1):
                east_gold = gold_cache[row][col + 1]

            # gold collected if we go NE
            if (row != 0 and col != len(field) - 1):
                ne_gold = gold_cache[row-1][col+1]

            # gold collected if we go NE
            if (row != len(field) - 1 and col != len(field) - 1):
                se_gold = gold_cache[row+1][col+1]

            current_gold_on_block = field[row][col]

            # Add current gold plus BEST amount from E, NE, or SE.
            # Save it in cache.
            gold_cache[row][col] = current_gold_on_block + \
                max(east_gold, ne_gold, se_gold)
    best_gold = gold_cache[0][0]

    return f'{best_gold} gold is the most we can get.'
