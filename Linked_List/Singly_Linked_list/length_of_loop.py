# if there exixts a cycle in the LL , then give the length to complete that cycle 
#1. BRUTe
def cyc(self, head):
    mydict = dict()
    travel = 0
    temp = head
    while temp is not None :
        if temp in mydict:
            return travel-mydict[temp]
        mydict[temp] = travel
        travel+=1
        temp = temp.next
    return 0



#2. OPTIMAL
def cyc(self, head):
    slow= head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            count=1
            while slow!=fast:
                count+=1
            return count
        




