class Node:
    def __init__(self, val):
        self.val = val
        self.next =None
        self.prev = None
class Linked:
    def __init__(self):
        self.head = None
    def insert_at_head(self, val):
        new = Node(val)
        if not self.head:
            self.head =new
        else:
            self.head.prev =new
            new.next = self.head
            self.head = new
    def append(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
            return
        else:
            temp = self.head
            while temp.next:
                temp=temp.next
            temp.next = new
            new.prev = temp
    def insert_in_between(self, val, pos):
        new= Node(val)
        temp = self.head
        c=0
        while temp is not None and c<pos-1:
            temp =temp.next
            c+=1
        if temp is None:
            print("pos out of bounds")
            return
        new.next = temp.next
        new.prev = temp
        if temp.next:
            temp.next.prev= new
        temp.next =new
    def traverse(self):
        if not self.head:
            print("no elements in the linked list")
        else:
            temp = self.head
            while temp is not None:
                print(temp.val)
                temp = temp.next
    def delete_head(self, val):
        if self.head is None:
            print("list is empty")
            return 
        self.head= self.head.next
        if self.head: # if list is not empty after deletion
            self.head.prev = None
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        if temp.prev: # more than one node\
            temp.prev.next= None
        else:
            self.head =None
    def delete_anywhere(self, val):
        if self.head is None:
            print("list is empty ")
            return 
        
        temp = self.head
        while temp:
            if temp.val == val:#deleteing head
                if temp.prev is None:
                    self.head= temp.next
                    if self.head:
                        self.head.prev= None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev=temp.prev
                return 
            temp = temp.next
        print("value not found")
        














            


