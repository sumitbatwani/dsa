class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

head = node1
current = head

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("End of linked list")