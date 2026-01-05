"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print()

print_linked_list(head)

# 1 -> 2 -> 3

def reverse_linked_list(head):
    remaining_list = head
    prev = None
    while remaining_list:
        current = remaining_list
        remaining_list = remaining_list.next
        current.next = prev
        prev = current
    
    return prev
    
new_head = reverse_linked_list(head)
print_linked_list(new_head)
