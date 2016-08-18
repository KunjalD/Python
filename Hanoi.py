#!/usr/bin/env python

class Hanoi:
    def __init__(self,size):
        self.size = size
        self.towers = [[],[],[]]
        self.towers[0] = [i for i in range(size, 0, -1)]

    def playHanoi(self):
        self.printHanoi()
        self.moveDisk(self.size,1,2,3)
        self.printHanoi()

    def moveDisk(self,size,fr,helper,to):
        if size == 1:
            data = self.towers[fr-1].pop()
            self.towers[to-1].append(data)
        else:
            self.moveDisk(size-1,fr,to,helper)
            print (size-1,fr,to,helper)
            self.moveDisk(1,fr,helper,to)
            print (1,fr,helper,to)
            self.moveDisk(size-1,helper,fr,to)
            print (size-1,helper,fr,to)

    def printHanoi(self):
        for i in self.towers:
            print i

hanoi = Hanoi(5)
hanoi.playHanoi()
