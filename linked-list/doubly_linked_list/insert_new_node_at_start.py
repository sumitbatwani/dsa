class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

node2 = Node(2)
head = node2

node3 = Node(3)
node3.prev = node2
node2.next = node3

def print_list(head):
    current = head
    while current:
        print(current.data, end="")
        if current.next:
            print(" <-> ", end="")
        current = current.next
    print()

print_list(head)

def insert_at_start(head, new_node):
    if head:
        new_node.next = head
        head.prev = new_node

    return new_node

node1 = Node(1)
head = insert_at_start(head, node1)
print_list(head)

