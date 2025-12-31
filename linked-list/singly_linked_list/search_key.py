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

def search_key(head, key):
    current = head
    while current:
        if current.data == key:
            return print("Found key...")
        current = current.next
    return print("Key not found...")

def search_recursively(head, key):
    if head is None:
        return print("(R) Key not found...")

    if head.data == key:
        print("(R) Found key...")
    else:
        search_recursively(head.next, key)

node1 = Node(1)
head = node1

node2 = Node(2)
node1.next = node2

print("Original list:")
print_list(head)
search_key(head, 2)
search_key(head, 3)

search_recursively(head, 2)
search_recursively(head, 3)
