class Node(object):

    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self, next_node):
        self.next_node = next_node

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self,data):
        current = self.head
        found = false;
        if(current.get_data() == data)
        {
            found = True
        }else{
            current = current.get_next()
        }
        if current is None:
            raise valueError ("no data found")
        return current

    def delete(self,data):
        current = self.heaf
        found = False
        while current and found is False:
            if current.get_data == data:
                found = True
            else
                previous = current
                current = current.get_next()
        if current is None:
            raise valueError ("No data")
        if previous is None:
            self.head = current.get_next()
        else
            previous.set_next(current.get_next)

    def size(self):
        current = self.head
        count =0
        while current:
            count +=1
            current = current.get_next()
        return count




