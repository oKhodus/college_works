class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, value):
        new_node = Node(value)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def delete(self, value):
        if self.head.value == value:
            self.head.value = self.head.next

    def display(self):
        current_node = self.head
        count = 1
        while current_node != None:
            name = f"list_head-node_{count}" if count == 1 else f"node_{count}"
            print(f"|{name}: {current_node.value}|", end=" ")
            current_node = current_node.next
            count += 1

        print(f"|list_tail: {current_node}|")


ll = LinkedList()

print(
    "Hello welcome to [LinkedListApp]\nif you wanna start creation of Linked List - enter commands:\n\
\n['-head'] if wanna add to head of list\n['-tail'] if wanna add to tail of list\n"
)

cmd = input("Enter a command: ")
if cmd == "-head":
    path = "head"
elif cmd == "-tail":
    path = "tail"

while True:
    elem = input(f"\nEnter numbers for {path} or '-added' to finish adding to list: ")
    if elem != "-added" and path == "head":
        ll.insert_head(elem)
    elif elem != "-added" and path == "tail":
        ll.insert_tail(elem)
        # elem = input("Enter numbers for head or \'added\' to finish adding to list: ")
    else:
        ll.display()
        break

# except Exception:
#     pass
