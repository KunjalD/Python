from linkedList import *

def findBegin(L1):
    slow = linkedList.head
    fast = linkedList.head

    while (fast != None) and (fast.next !=None):
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if fast == None and fast.next == None:
        return None

    fast = linkedList.head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return fast
