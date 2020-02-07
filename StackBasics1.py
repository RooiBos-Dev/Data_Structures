class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def getStack(self):
        print(self.items)
    def isEmpty(self):
        return self.items == []

def main():
    obj = Stack()
    obj.push("Cal")
    obj.push("Dylan")
    obj.push("Yusrie")
    obj.push("Eric")    
    obj.getStack()
    obj.pop()
    obj.pop()
    obj.getStack()

    print(obj.isEmpty())

if __name__ == '__main__':
    main()