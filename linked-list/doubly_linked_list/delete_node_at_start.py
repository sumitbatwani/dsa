# (head)1<->2<->3->none
class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

def print_list(head):
    current = head
    while current:
        print(current.data, end="")
        if current.next:
            print(" <-> ", end="")
        current = current.next
    print()

node1 = Node(1)
head = node1

node2 = Node(2)
node1.next = node2
node2.prev = node1

node3 = Node(3)
node2.next = node3
node3.prev = node2

print_list(head)

def delete_at_start(head):
    # (head)1 <-> 2 <-> 3
    if not head:
        return head
    
    new_head = head.next
    
    if new_head:
        new_head.prev = None

    head.next = None
    return new_head

head = delete_at_start(head)
print_list(head)