def delete(self, key, head):
    if head.next is None and head.val==key: # single element
        return head
    temp = head
    prev=None
    new_head = head
    while temp:
        if temp.val == key:
            if prev is not None: # if element is not in the head 
                prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = prev
            if temp ==  new_head:  # when the simailar element comes at start

                new_head = new_head.next
        prev= temp
        temp = temp.next

