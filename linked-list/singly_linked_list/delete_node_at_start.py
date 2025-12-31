class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
head = node1

node2 = Node(2)
node1.next = node2

node3 = Node(3)
node2.next = node3

def print_nodes(head):
    current = head
    while current:
        print(current.data, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print()

print_nodes(head)

def delete_at_start(head):
    # head[1, ->][2, ->][3, ->]None
    # head[2, ->][3, ->]None
    temp = head
    head = head.next
    temp = None # free up memory
    return head

head = delete_at_start(head)
print_nodes(head)
