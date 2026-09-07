class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head= None
    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node


    def traverse(self):
        if self.head == None:
            print("list is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next
            print()

    def insert(self, val, pos):
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.head # insertion at beginning
            self.head = new_node
        else:   # insertion at specific
            count = 0
            curr = self.head
            prev_node = None
            while curr is not None and count<pos:  # we will move forward until we are in the right pos
                prev_node = curr   # pos is between prev_node and the curr
                curr = curr.next
                count+=1
            prev_node.next = new_node
            new_node.next = curr
    def delete(self, val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:

                self.head = self.head.next  # del from beginning
                return 
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev.next=temp.next
                    return
                else:
                    print("node not found")



sll = LinkedList()
sll.append(10)
sll.append(18)
sll.append(2)
sll.append(1)
sll.traverse()
sll.delete(2)
sll.insert(8,0)
sll.traverse()














            

            

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



