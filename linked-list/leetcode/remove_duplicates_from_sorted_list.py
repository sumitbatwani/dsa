"""
Given the head of a sorted linked list, delete all duplicates such 
that each element appears only once. 

Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]
"""

"""
Algorithm:
# [1,1,1,2,2,3] -> [1,2,3]
1. If the list is empty or has only one node, return head
2. Initialize a pointer current to the head of linked list
3. Traverse until current.next exists:
    1. Compare current node data with next node data:
        - If they are equal, update current next to next node next, do not update current (as there can be more duplicates)
        - If they are different, update current to current.next
    Continue until end of list is reached
4. Return the head of the updated linked list
"""