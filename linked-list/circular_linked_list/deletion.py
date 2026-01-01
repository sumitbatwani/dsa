class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    current = head
    while True:
        print(current.data, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
        if current == head:
            break
    print("(back to head)")

node1 = Node(1)
head = node1

node2 = Node(2)
node1.next = node2

node3 = Node(3)
node2.next = node3

node4 = Node(4)
node3.next = node4

node5 = Node(5)
node4.next = node5

node6 = Node(6)
node5.next = node6

node5.next = head

print_list(head)

def delete_from_start(head):
    if not head:
        return None
    
    if head.next == head:
        return None
    
    new_head = head.next
    current = head

    while current.next != head:
        current = current.next
    
    current.next = new_head
    head = None

    return new_head

# head = delete_from_start(head)
# print_list(head)

def delete_from_end(head):
    if not head:
        return None
    
    current = head
    if current.next == head:
        return None
    
    prev = None
    while current.next != head:
        prev = current
        current = current.next
    
    prev.next = head
    current.next = None

    return head

# head = delete_from_end(head)
# print_list(head)    

def delete_at_position(head, position):
    if not head:
        return None
    
    if head.next == head:
        if position == 1:
            return None
        else:
            return head
    
    if position == 1:
        current = head
        while current.next != head:
            current = current.next

        new_head = head.next
        current.next = new_head
        head.next = None
        return new_head
    
    else:
        current = head
        i = 1

        while i < position - 1 and current.next != head:
            current = current.next
            i += 1

        if current.next == head:
            return head

        node_to_delete = current.next
        current.next = node_to_delete.next
        node_to_delete.next = None

        return head


head = delete_at_position(head, 3)
print_list(head)