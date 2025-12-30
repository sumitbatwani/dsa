class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node4 = Node(4)

head = node1
node1.next = node2
node2.next = node4

current = head
while current:
    print(current.data, end="")
    if current.next:
        print(" -> ", end="")
    current = current.next
print()

node3 = Node(3)
position = 1
# [1, ->][2, ->][4,->]None
# [1, ->][2, ->][3, ->][4,->]None

left = head
right = head.next

if position == 1:
    node3.next = head
    head = node3
else: 
    i = 1
    while i < position-1:
        i += 1
        left = right
        right = right.next

    left.next = node3
    node3.next = right

print('After insertion...')
current = head
while current:
    print(current.data, end="")
    if current.next:
        print(" -> ", end="")
    current = current.next
print()
