class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    current = head
    while current:
        print(current.data, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print()

node1 = Node(1)
head = node1

node2 = Node(2)
node1.next = node2

node3 = Node(3)
node2.next = node3

node4 = Node(4)
node3.next = node4

print(f"{'-'*80}")
print("Original list:")
print_list(head)

def delete_at_position(head, position):
    # [1, ->][2, ->][3, ->][4, ->]None
    # [1, ->][2, ->][4, ->]None
    current = head
    prev = head
    i = 1
    while i < position:
        i += 1
        prev = current
        current = current.next

    prev.next = current.next
    current = None
    return head

head = delete_at_position(head, 3)
print_list(head)
