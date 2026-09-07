def dupli(self, head):
    dummy  = Node(0)
    dummy.next = head
    temp = head
    prev = dummy
    while temp:
        if temp.next and temp.val == temp.next.val:
            while temp.next and temp.val == temp.next.val:
                temp = temp.next
            prev.next = temp.next
        else:
            prev = prev.next
        temp = temp.next
    return dummy.next








