"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

listA = [4,1,8,4,5], 
listB = [5,6,1,8,4,5]

head = None

current1 = 4
current2 = 5
if current1 == current2: head = current1
4 -> 1 -> 8
5 -> 6 -> 1 -> 8    

Find length of both the lists
calculate difference in length of two lists 
start the traversal from the differnce (advance the pointer to difference)
compare node from two lists
if match return that node
else terminate if node.next is None and return null
"""