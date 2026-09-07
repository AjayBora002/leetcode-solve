def merge(l1, l2):
    dummy = Node()  # creates a temporary node
    temp= dummy
    while l1 and l2:
        if l1.val<l2.val:
            temp.next = l1 # attaches l1 to teh merged list
            l1=l1.next 
        else:
            temp.next = l2
            l2= l2.next
        temp = temp.next
    if l1:  # gets the remaining in the l1 and l2
        temp.next =l1
    else:
        temp.next= l2
    return dummy.next  # returns the merged actual list not the dummy






