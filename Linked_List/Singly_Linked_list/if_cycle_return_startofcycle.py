# leetcode @142
# if a linked list is cya=clic then retun the node where the cycle starts

#1, BRUTE
def cyc(self, head):
    temp = head
    mysets = set() # creating an empty sets to store the npdes
    while temp is not None:
        if temp in mysets:
            return temp
        mysets.add(temp)
        temp= temp.next
    return None




#2. OPTIMAL
def cyc(self, head):
    slow = head
    fast= head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow!=fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None










            



