# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

head = node1
node1.next = node2
node2.next = node3

current = head
while current is not None:
    print(current.data, end = " ")
    if current.next is not None:
        print(" -> ", end="")
    current = current.next

print()
