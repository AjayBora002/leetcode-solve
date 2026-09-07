def pair(self, val , target, head):
    temp1 = head
    r=[]
    while temp1 is not None:
        temp2 = temp1.next
        while temp2 is not None:
            if temp1.val+temp2.val == target:
                r.append([temp1, temp2])
            temp2 = temp2.next
        temp1 = temp1.next
    return r



