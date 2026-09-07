class NOde:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class SS:
    def __init__(self):
        self.head = None
    def remove(self, head):
        temp = self.head
        while temp and temp.next:
            if temp.val == temp.next.val:
                next_node = temp.next
                temp.next = next_node.next
                if next_node.next:
                    next_node.next.prev = temp
            else:
                temp = temp.next
        return self.head
    




class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        temp = head
       
        while temp and temp.next :
            if temp.val == temp.next.val:
                temp.next = temp.next.next 
            else:
                temp = temp.next
        return head