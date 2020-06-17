from word2number import w2n

# Print out all of the strings in the following array that represent a number divisible by 3:

num_list = [
    "five",
    "twenty six",
    "nine hundred ninety nine",
    "twelve",
    "eighteen",
    "one hundred one",
    "fifty two",
    "forty one",
    "seventy seven",
    "six",
    "twelve",
    "four",
    "sixteen"
]


# The expected output for the above input is:
# nine hundred ninety nine
# twelve
# eighteen
# six
# twelve
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# x = "5"
# y = "five"

# x.isdigit()
# y.isdigit()
# # y.isdigit() not work because it is evaluating whether or not a "5" would be a digit. "5" is a digit, "five" is not. Therefore
# print(w2n.word_to_num(y))

# O(n) time complexity because the number of operations expands based on the value of n -- in this case, the number of items inside num_list
# 0(1) space complexity because no new items are being created. We're working within the bounds of something that already exists and just validating.

for i in num_list:
    if w2n.word_to_num(i) % 3 == 0:
        print(i)
