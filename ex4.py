list=[0]

def polyvaleur(listpoly, x):
    n=0
    for i in range(len(listpoly)):
       n+=listpoly[i]*x**i
    return n

print(polyvaleur ([1,0,2,3], 2))

def polyaddition(listpoly1, listpoly2):
    s=[]
    n=0
    if len(listpoly1)>len(listpoly2):
        n=len(listpoly1)
        for i in range(n-len(listpoly2)):
            listpoly2.append(0)
    else:
        for i in range(n-len(listpoly1)):
            listpoly1.append(0)
        n=len(listpoly2)
        
        
    for i in range(n):
        a=listpoly1[i]+listpoly2[i]
        s.append(a)
    return s
    
      
          
print(polyaddition([1,2,5],[3,4]))       
    
def polyaffiche(listpoly):
    ch=""
    if listpoly[0]!= 0 :
            ch+=str(listpoly[0])
    for i in range(1,len(listpoly) ):
        if listpoly[i]!= 0 :
            ch+="+"+str(listpoly[i])+"X^"+str(i)
        
    return ch


 
 
 
 
 
print(polyaffiche ([3,0,4,0,2]))   
