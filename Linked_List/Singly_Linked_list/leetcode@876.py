def middle(self, head):
    count = 0
    temp = head
    while temp is not None:
        count+=1
        temp = temp.next
    temp = head
    for i in range(count//2):
        temp = temp.next
    return temp






# for interviews apply tortoise and hare approach
def middle(self, head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow









