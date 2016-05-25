class fiboNode:
    def __init__(self,key):
        self.key=key
        self.degree=0
        self.right=None
        self.left=None
        self.parent=None
        self.child=None
        self.mark=False


class fiboHeap:

    def __init__(self,key):
        self.min=fiboNode(key)
        self.keyNum+=1
        self.min.left=self.min
        self.min.right=self.min

    def insert(self,key):
        insertNode=fiboNode(key)
        self.min.right.left=insertNode
        insertNode.right=self.min.right
        self.min.right=insertNode
        insertNode.left=self.min
        if(insertNode.key<self.min.key):
            self.min=insertNode
        self.keyNum+=1


    def deleteMin(self,key):

    def deleteNode(self,node):

    
        
