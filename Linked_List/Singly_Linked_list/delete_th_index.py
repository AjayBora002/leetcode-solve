# delete the nth index and the indexing start from the last
# 1.
def delete(self, head, n):
    temp = head
    count = 0
    while temp is not None:
        count+=1
        temp = temp.next
    if count == n:
        return head.next
    temp = head
    for _ in range(count -n -1):
        temp = temp.next
    temp.next = temp.next.next
    return head


#2. optimal(one pass)
def delete(self, head, n):
    slow = head
    fast = head
    for _ in range(n):
        fast = fast.next
    if fast == None:
        return head.next
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head









