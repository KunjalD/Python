from linkedList import *

def deleteDups(linkedList):
    if (linkedList != None)
        currNode = linkedList.head
        dic = {currNode.value: True}
        while currNode.next != None:
            if currNode.next.value in dic:
                currNode.next = currNode.next.next
            else:
                dic[currNode.next.value] = True
                currNode = currNode.next


def deleteDups(linkedList):
    currNode = linkedList.head
    if (currNode != None):
        runner = currNode
        while runner.next != None:
            if runner.next.value == currNode.value:
                runner.next = currNode.next.next
            else
                runner = runner.next
        currNode = currNode.next





