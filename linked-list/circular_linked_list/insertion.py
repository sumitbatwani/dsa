class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def print_circular_list(head):
    if not head:
        print("List is empty")
        return
    
    current = head
    while True:
        print(current.data, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
        if current == head:
            break
    print("(back to head)")

node2 = Node(2)
head = node2

node3 = Node(3)
node2.next = node3

node4 = Node(4)
node3.next = node4
node4.next = node2

print_circular_list(head)

# 2 -> 3 -> 4 -> (back to head)

def insert_at_start(head, new_node):
    if not head:
        new_node.next = new_node
        return new_node

    current = head
    while current.next != head:
        current = current.next
    
    new_node.next = head
    head = new_node
    current.next = new_node

    return head

# print_circular_list(insert_at_start(head, Node(1)))

def insert_at_end(head, new_node):
    if not head:
        new_node.next = new_node
        return new_node
    
    current = head
    while current.next != head:
        current = current.next

    current.next = new_node
    new_node.next = head

    return head

# print_circular_list(insert_at_end(head, Node(5)))

def insert_at_position(head, new_node, position):
    if not head:
        new_node.next = new_node
        return new_node
    
    if position == 1:
        current = head
        while current.next != head:
            current = current.next

        new_node.next = head
        head = new_node
        current.next = head
        
    else:
        i = 1
        current = head
        while i < position - 1 and current.next != head:
            current = current.next
            i += 1

        new_node.next = current.next
        current.next = new_node
        
    return head

print_circular_list(insert_at_position(head, Node(6), 4))
