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

print_list(node1)

def delete_at_position(head, position):
    if not head:
        return None
    
    if position == 1:
        new_head = head.next
        if new_head:
            new_head.prev = None

        head.next = None
        return new_head
    
    current = head
    i = 1

    while i < position and current:
        current = current.next
        i += 1

    if not current:
        return head
    
    # 1,2,(current:3)
    prev_node = current.prev
    next_node = current.next

    if next_node:
        prev_node.next = next_node
        next_node.prev = prev_node
    else:
        prev_node.next = None    

    current.prev = None
    current.next = None

    return head

head = delete_at_position(head, 3)
print_list(head)