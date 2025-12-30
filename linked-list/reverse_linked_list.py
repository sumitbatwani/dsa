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

def print_list(head):
    current = head
    while current:
        print(current.data, end="")
        if current.next:
            print(' -> ', end="")
        current = current.next
    print()

print_list(head)

# change the direction
# head:[1, ->][2, ->][3, ->]None
# None:[1, <-][2, <-][3, <-]head
def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

rev_list = reverse_list(head)
print_list(rev_list)
