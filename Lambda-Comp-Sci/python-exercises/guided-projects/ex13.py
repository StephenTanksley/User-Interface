# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.

# Example:

# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

class Solution:

    def __init__(self):
        self.seen_values = set()

    def isHappy(self, n: int) -> bool:

        if n == 1:
            return True

        if n in self.seen_values:
            return False

        self.seen_values.add(n)

        new_num = sum([int(digit)**2 for digit in str(n)])

        return self.isHappy(new_num)
