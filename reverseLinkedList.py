class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    def rever(self):
        if(self.head is None):
            return self.head
        else:
            current = self.head
            prev = None
            next = None
            while(current is not None):
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.head = prev


