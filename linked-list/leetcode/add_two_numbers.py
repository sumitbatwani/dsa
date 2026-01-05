# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

"""
Algorithm:
1. Initialize carry = 0
2. Traverse both lists together
3. At each step:
    Add current digits and carry
    Store the last digit in a new node
    Update carry
4. Continue until both lists are exhausted and carry is zero
5. Return the newly formed list
"""


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
