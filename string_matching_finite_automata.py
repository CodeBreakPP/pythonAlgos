
class smia:

    def __init__(self):
        self.trans={}
        self.length=0
        
    def setTrans(self,s):
        m=len(s)
        self.length=len(s)
        sigma=set(s)
        self.trans={}
        for i in range(m+1):
            self.trans[i]={}
            for j in sigma:
                self.trans[i][j]={}
                k=min(m+1,i+2)
                while k>=1:
                    k=k-1
                    if s[0:k]==(s[0:i]+j)[i+1-k:i+1]:
                        break
                self.trans[i][j]=k
                
    def match(self,s):
        k=0
        for i in range(len(s)):
            c=s[i]
            k=self.trans[k][c]
            if k==self.length:
                return i
        return -1
        
    
    
