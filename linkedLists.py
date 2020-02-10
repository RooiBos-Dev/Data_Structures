class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode
    def prepend(self,data):
        newNode = Node(data)
        newNode.next = self.head #points to head
        self.head = newNode #inserts new head Node
    def insertAt(self, previous, data):
        if not previous:
            print("Node does not exist in the list")
        newNode = Node(data)
        newNode.next = previous.next
        previous.next = newNode
    def deleteNode(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while(current and current.data != key):
            prev = current
            current = current.next 
        prev.next = current.next
        current = None
    def deleteaAtPos(self, pos):
        current = self.head
        count = 1
        prev = None
        while current and count != pos:
            prev = current
            current = current.next
            count += 1
        if current is None:
            return
        prev.next = current.next
        current = None
    def reverseList(self):
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = current.next
            current= temp
        self.head = prev





lst = LinkedList()
lst.add("Calvin")
lst.add("YO")
lst.add("This is number 3")
lst.add("I am oof I mean groot.")
lst.prepend("Hi")
lst.deleteaAtPos(2)
lst.reverseList()
lst.printList()
