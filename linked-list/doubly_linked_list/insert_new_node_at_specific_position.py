# Need practise
class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

def print_list(head: Node):
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

node4 = Node(4)
node2.next = node4
node4.prev = node2

print_list(head)

def insert_at_position(head, new_node, position):
    if position == 1:
        new_node.next = head
        head.prev = new_node
        return new_node

    current = head
    i = 1
    while i < position-1 and current:
        current = current.next
        i += 1

    if not current:
        return head
    
    # 1 <- 3 -> 2
    new_node.prev = current
    new_node.next = current.next

    # 1 <- 3 -> 2
    if current.next:
        current.next.prev = new_node
    current.next = new_node
    
    return head

head = insert_at_position(head, Node(3), position=4)
print_list(head)