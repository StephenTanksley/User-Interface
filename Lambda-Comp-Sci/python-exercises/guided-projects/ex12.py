# records = [
#     {"Alice", "Engineering"},
#     {"Sarah", "Sales"},
#     {"Carol", "Sales"},
#     {"Dave", "Sales"},
#     {"Erin", "Sales"},
#     {"Frank", "Engineering"},
#     {"Grace", "Engineering"},
#     {"Charles", "Engineering"},
#     {"Brian", "Marketing"},
#     {"Jordan", "Marketing"},
# ]


# def build_index(recs):
#     index = {}

#     for record in recs:
#         name, dept = record

#         # Check if department is already in index
#         if dept in index:
#             # if it is, add name to the list.
#             index[dept].append(name)
#         else:
#             index[dept] = [name]

#     return index


# department_index = build_index(records)

# print(department_index)


# import math

# # Lookup tables - We want to use a lookup table to remember the results of CPU-heavy computations.


# # this function is relatively time consuming.
# def get_inverse_square(num):
#     return 1/math.sqrt(num)


# # If we know we have to recompute the results of a function over and over, we can use a dictionary/hash map to help in this process.

# # What should the lookup table look like?
# # Keys will be numbers plugged into the function.
# # Values will be the value returned by get_inverse_square.

# def build_lookup_table():
#     lookup_table = {}
#     for i in range(1, 1000):
#         lookup_table[i] = get_inverse_square(i)
#     return lookup_table


# sqrt_lookup_table = build_lookup_table()

# print(sqrt_lookup_table[825])
# print(sqrt_lookup_table[12])
# print(sqrt_lookup_table[588])
# print(sqrt_lookup_table[25])
# print(sqrt_lookup_table[901])


# Given a string, can we figure out how many times each letter appears in it?

# def letter_count(s):
#     d = {}
#     for char in s:
#         if char.isspace():
#             continue
#         if char not in d:
#             d[char] = 1
#         else:
#             d[char] += 1
#     return d


# def double_letter(s):

#     d = set()
#     # Store letters as keys and a counter as value.
#     # Find letter(s) where value > 1.
#     for char in s:
#         if char.isspace():
#             continue
#         if char not in d:
#             d.add(char)
#         else:
#             return char

#     # for key, value in d.items():
#     #     if value == 2:
#     #         return key


# print(double_letter("abecdef"))


# Substitution Ciphers

# or how to transform data from one thing to another.

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

# decode_table = {}

# for key, value in encode_table.items():
#     decode_table[value] = key

decode_table = {v: k for k, v in encode_table.items()}

print(decode_table)


def encode(plain_text):
    cipher = ""

    for char in plain_text:
        if char.isspace():
            cipher += " "
        else:
            cipher += encode_table[char.upper()]
    return cipher


print(encode("Dictionaries are awesome"))


def decode(cipher_text):
    cipher = ""

    for char in cipher_text:
        if char.isspace():
            cipher += " "
        else:
            cipher += decode_table[char.upper()]
    return cipher


print(decode("WPYFPECHUPON HUO HBONELO"))
