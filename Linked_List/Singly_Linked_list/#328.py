def even_odd(self,head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = odd.next.next
        odd=odd.next
        even.next= even.next.next # matched the 1st element with the third and go on 
        even = even.next # when the upper line executes , the two odd ones comes next to each other , so to get that elemet
        
    odd.next=even_head # matches the last element of odd to the 1st elemen of the even
    return head










