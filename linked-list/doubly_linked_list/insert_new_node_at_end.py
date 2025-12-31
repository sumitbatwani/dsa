class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

node1 = Node(1)
head = node1

node2 = Node(2)
node1.next = node2
node2.prev = node1

def print_list(head, message=None):
    print(message)
    current = head
    while current:
        print(current.data, end="")
        if current.next:
            print(" <-> ", end="")
        current = current.next
    print()

print_list(head, "Original list:")

def insert_at_end(tail, new_node):
    if tail:
        tail.next = new_node
        new_node.prev = tail
        
    return new_node

current = head
while current.next:
    current = current.next

tail = current
node3 = Node(3)
tail = insert_at_end(tail, node3)
print_list(head, "Inserted at end:")