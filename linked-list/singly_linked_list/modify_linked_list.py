class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# [10, 4, 5, 3, 6, 8]
node1 = Node(10)
node2 = Node(4)
node3 = Node(5)
node4 = Node(3)
node5 = Node(6)
node6 = Node(8)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

def print_list(head):
    current = head
    while current:
        print(current.data, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print()

print_list(head)

# first half [start - end]
# middle [no change]
# second half [swap]

temp_list = []
current = head
while current:
    temp_list.append(current.data)
    current = current.next

temp_list.reverse()
is_odd = True if len(temp_list) % 2 > 0 else False
middle = int(len(temp_list)/2)

current = head
i = 0
while current:
    if i < len(temp_list):
        if i < middle:
            current.data = temp_list[i] - current.data
        else:
            current.data = temp_list[i]

    i+=1
    current = current.next

print_list(head)
