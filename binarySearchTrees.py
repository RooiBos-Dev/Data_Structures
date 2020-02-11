class Node():
   def __init__(self,data):
      self.data = data
      self.right = None
      self.left = None


class Tree():
    def __init__(self):
        self.root = None
    def insert(self,item):
        if self.root is None:
            self.root = Node(item)
        else:   
            self.insertAfter(self.root,item )

    def insertAfter(self,root,item ):
        if item > root.data:
            if root.right == None :
                root.right = Node(item)
            else:   
                self.insertAfter(root.right,item)
        elif item < root.data:
            if root.left is None:
                root.left = Node(item)
            else:   
                self.insertAfter(root.left,item)
        else:
            print("This value aready exists in the tree.")
    def find(self,item):
        if(self.root):
            find = self.findItem(self.root,item)
            if(find == True):
                return True
            else:
                return False
        else:
            False
    def findItem(self,root,item):
        if(item > root.data and root.right):
            return self.findItem(root.right,item)
        elif(item < root.data and root.left):
            return self.findItem(root.left,item)
        if(item == root.data):
            return True


obj = Tree()
obj.insert(4)
obj.insert(5)
obj.insert(13)
obj.insert(14)
print(obj.find(15))
