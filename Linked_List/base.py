class Node:  # started a node
    def __init__(self, val):
        self.val=val  # initialized the value part
        self.next=None  # initialized the next part as None
node1 = Node(5)
node2 = Node(10)  # these are the values of the linked list
node3 = Node(8)
node4=Node(20)

node1.next = node2
node2.next = node3  # given the next part or the address of the next node part
node3.next = node4

print(node1)
print(node1.val)
print(node2.next.val)




class No:
    def __init__(self, val):
        self.val = val
        self.next = next
n1 = No(3)
n2 = No(6)

n1.next = n2
print(n1.val)






class Nod:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, val):
        new_node = Nod(val)
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
            print("")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end =" ")
                curr = curr.next
            print()

    def insert(self, val, pos):
        new_node = Nod(val)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            curr= self.head
            prev_node = None
            while curr is not None and count<pos:
                prev_node = curr
                curr=curr.next
                count+=1
            prev_node.next = new_node
            new_node.next = curr
    def delete(self, val):
        temp = self.head
        if temp is not None:
            if temp == val:
                self.head = self.head.next
                return 
        else:
            found = False
            prev = None
            while temp is not None:
                if temp == val:
                    found = True
                    break
                prev = temp
                temp = temp.next
            if found:
                prev.next = temp.next
                return 
            else:
                print("element not found")










