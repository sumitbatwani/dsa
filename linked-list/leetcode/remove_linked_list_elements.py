"""
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, 
and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Algorithm:
1. head == current, prev == current
2. Loop untill current != None
[6,1,2,6,6,3,4,5,6] =>> 6
3. if current.data == val, 
    if prev then prev.next == current.next else prev == current.next and head == prev
4. if current.data != val, current = current.next
5. return head

"""

