#!/usr/bin/env python

class SetOfStacks:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, val):
        if len(self.stacks == 0) or (len(self.stacks[-1]) == self.capacity):
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self):
        if len(self.stacks == 0):
            return None
        data = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return data

    def popAt(self,index):
        if index < 1 or index > len(self.stacks) or len(self.stacks[index-1]) == 0:
            return None
        else:
            return self.stacks[index-1].pop()

def test():
    SetOfStacks = SetOfStacks(8)
    for i in range(24):
        SetOfStacks.push(i)
        print i
    print ""

    for i in range(5):
        for i in range(3):
            print "Popped", SetOfStacks.popAt(i+1)

if __name__ =="main"
    test()
