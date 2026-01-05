"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

"""
Algorithm:
1. Maintain a pointer to the head of the merged list
2. Compare the current nodes of both lists
3. Attach the smaller node to the merged list and advance that list
4. Repeat until one list ends
5. Attach the remaining nodes of the other list
6. Return the merged list head
"""