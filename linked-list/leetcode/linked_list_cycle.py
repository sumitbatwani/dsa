"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list 
that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true

Input: head = [1], pos = -1
Output: false

Algorithm:
1. Initialize seen = []
2. loop through list untill current is None:
3. return true if current is in seen
4. else add current node in seen
5. return false
"""