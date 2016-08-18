#!/usr/bin/env python

class MyQueue(object):
    def __init__(self):
        self.front_stack = Stack()
        self.back_stack = Stack()

    def eq(self,data):
        self.back_stack.push(data)

    def dq(self):
        if self.front_stack.size == 0:
            self.rebuild()
        return self.front_stack.pop()

    def peek_front(self):
        if self.front_stack.size == 0:
            self.rebuild()
        return self.front_stack.peek()

    def rebbuild(self):
        while self.back_stack.size > 0:
            self.front_stack.push(self.back_stack.pop())

class Node(object):
    def __init__(self,data=None,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)

class Stack(object):
    def __init__(self):
        self.stack = Node()
        self.size = 0

    def push(self,data):
        self.stack = Node(data, self.stack)
        self.size +=1

    def pop(self):
        assert self.stack.data is not None, "Empty stack"
        value = self.stack.data
        self.stack.data = self.stack.nextNode.data
        self.stack.nextNode = self.stack.nextNode.nextNode
        self.stack.size -=1
        return value

    def peek(self):
        assert self.stack.size > 1, "Empty stack"
        return self.stack.data

    def __str__(self):
        stack_copy = deepcopy(self)
        tempHolder =[]
        while stack_copy.size > 0:
            tempHolder.append(stack_copy.pop())
        return ", ".join(map(str,tempHolder[::-1]))

if __name__ == "__main__":
    a = MyQueue()
    a.eq(1)
    a.eq(2)
    print a.dq()
    print a.peek_front()


class Stack(list):
    def peak(self):
        return self[-1]

    def push(self,data):
        self.append[data]

    def empty(self):
        return len(self) == 0
    def sort_stack(s):
        r = Stack()
        tmp = s.pop()
        while not s.empty():
            while not r.empty() and r.peak() > tmp:
                s.push(r.pop())
            r.push(tmp)
            while not s.empty() and s.peak() >= r.peak():
                r.push(s.pop())
        return r

from random import randrange
test_items = [randrange(20) for i in xrange(20)]
print test_items
S = Stack()
for i in test_items:
    S.push(i)
S = Stack.sort_stack(S)
for i,item in enumerate(sorted(test_items)):
    print "item", i, S[i]


class AnimalQueue(object):
    def __init__(self):
        from collection import deque
        self.dog_q = deque()
        self.cat_q = deque()
        self.time_stamp = 0

    def enqueue(self,animal_type,animal_name):
        if animal_type == "Dog":
            self.dog_q.appendleft((animal_name,self.time_stamp))
            self.time_stamp +=1
        elif animal_type == "cat":
            self.cat_q.appendleft((animal_name,self.time_stamp))
            self.time_stamp +=1
        else:
            print "invalid animal_type"

    def deque_any(self):
        dog = self.dog_q.pop() if not len(self.dog_q) == 0 else (None, -1)
        cat = self.cat_q.pop() if not len(self.cat_q) == 0 else (None, -1)
        if dog[1] == -1 and cat[1] == -1:
            return None
        elif dog[1] < cat[1]:
            self.cat_q.append(cat)
            return dog[0]
        else:
            self.dog_q.append(dog)
            return cat[0]

    def dequeue_cat(self):
        if not len(self.cat_q) == 0:
            return self.cat_q.pop()[0]

