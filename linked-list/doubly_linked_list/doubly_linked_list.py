class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# head:[<-, 1, ->][<-, 2, ->][<-, 3, ->]None

head = node1

# forward linking
node1.next = node2
node2.next = node3

# backward linking
node2.prev = node1
node3.prev = node2

# forward traversal
print('Forward traversal:')
current = head
while current:
    print(current.data, end="")
    if current.next:
        print(" <-> ", end="")
    current = current.next
print()

# backward traversal
print('Backward traversal:')
current = node3

while current:
    print(current.data, end="")
    if current.prev:
        print(" <-> ", end="")
    current = current.prev
print()
    
