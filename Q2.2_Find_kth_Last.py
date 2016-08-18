from linkedList import *

def kth_to_last(linkedList,k):
    if k <= 0:
        return "invalid k"
    pointer2 = linkedList.head
    for i in range(k-1):
        if pointer2.next != None:
            pointer2 = pointer2.next
        else:
            return "k exceeds the linkedList length"

    pointer1 = linkedList.head
    while pointer2.next != None:
        pointer2 = pointer2.next
        pointer1 = pointer1.next
    return pointer1
