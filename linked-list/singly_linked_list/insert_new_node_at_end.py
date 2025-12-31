class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

head = node1
node1.next = node2
node2.next = node3

current = head
while current:
    print(current.data, end="")
    if current.next:
        print(" -> ", end="")
    current = current.next
print()

# [1, ->][2, ->][3, ->]None

node4 = Node(4)

last = head
while last.next:
    if last.next:
        last = last.next

last.next = node4 

current = head
while current:
    print(current.data, end="")
    if current.next:
        print(" -> ", end="")
    current = current.next
print()
