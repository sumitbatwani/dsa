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

print("Before update...")
current = head
while current is not None:
    print(current.data, end = "")
    if current.next is not None:
        print(" -> ", end="")
    current = current.next
print()

node0 = Node(0)
# [1, ->][2, ->][3, ->]None
# head

# [0, ->][1, ->]
# head
node0.next = head
head = node0

print('After update...')
current = head
while current is not None:
    print(current.data, end="")
    if current.next is not None:
        print(" -> ", end="")
    current = current.next
print()
