class fiboNode:
    def __init__(self,key):
        self.key=key
        self.degree=0
        self.right=self
        self.left=self
        self.parent=None
        self.child=None
        self.mark=False


class fiboHeap:

    def __init__(self,key):
        self.min=fiboNode(key)
        self.keyNum=1
        self.min.left=self.min
        self.min.right=self.min

    def insert(self,key):
        insertNode=fiboNode(key)
        if self.min==None:
            self.min=insertNode
        else:
            self.min.right.left=insertNode
            insertNode.right=self.min.right
            self.min.right=insertNode
            insertNode.left=self.min
            if(insertNode.key<self.min.key):
                self.min=insertNode
        self.keyNum+=1

    def link(self,x,y):
        x.right.left=x.left
        x.left.right=x.right
        x.parent=y
        y.degree+=1

        if y.child==None:
            y.child=x
            x.right=x
            x.left=x
        else:
            y.child.right.left=x
            x.right=y.child.right
            y.child.right=x
            x.left=y.child
        return y
        
    def getMin(self):
        return self.min.key

    def deleteMin(self):
        
        minkey=None
        if self.min!=None:
            
            minkey=self.min.key
            f=self.min.child
            
            if f!=None:
                while f.parent!=None:
                    f.parent=None
                    f=f.left

                self.min.left.right=self.min.child

                self.min.right.left=self.min.child.left

                self.min.child.left.right=self.min.right
                
                self.min.child.left=self.min.left
                    
                    
            else:
                self.min.right.left=self.min.left
                self.min.left.right=self.min.right

            if self.min.right==self.min:
                self.min=None
            else:
                self.min=self.min.right
                
                newminkey=self.min.key
                newminnode=self.min
                startmin=self.min.right

                while startmin!=self.min:
                    if startmin.key<newminkey:
                        newminkey=startmin.key
                        newminnode=startmin
                    startmin=startmin.right
            
                self.min=newminnode
                print "consolidate"
                self.consolidate()
            
            self.keyNum-=1
        

        return minkey
    
    def consolidate(self):
        A={}
        start=self.min.right
        A[self.min.degree]=self.min
        if start!=self.min:
            d=start.degree
            A.setdefault(d,None)

            while A[d]!=None:
                #print d
                if start.key<A[d].key:
                    start=self.link(A[d],start)
                else:
                    start=self.link(start,A[d])
                A[d]=None
                d=start.degree
                A.setdefault(d,None)
            A[d]=start


    
    def printRoots(self):

        f=[]
        f.append(str(self.min.key))

        start=self.min.left

        while start!=self.min:
            f.append(str(start.key))
            start=start.left
        print ",".join(f)

        

        
    
    #def deleteNode(self,node):

    
        
