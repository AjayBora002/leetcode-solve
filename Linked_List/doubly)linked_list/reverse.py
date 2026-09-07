def reverse(self, head):
    if head.next is None:
        return head
    temp = head
    prev = None
    while temp is not None:
        front=temp.next
        temp.next= prev
        temp.prev = front
        prev =temp
        temp= front
    return prev
    