def trans(s):
    m=len(s)
    sigma=set(s)
    print sigma
    trans={}
    for i in range(m+1):
        trans[i]={}
        for j in sigma:
            trans[i][j]={}
            k=min(m+1,i+2)
            while k>=1:
                k=k-1
                if s[0:k]==(s[0:i]+j)[i+1-k:i+1]:
                    break
            trans[i][j]=k
    return trans                
    
    
