def rev(self, head):
    curr = head
    prev = None
    while curr is not None:
        front = curr.next
        curr.next = prev
        prev = curr
        curr = front
    return prev










