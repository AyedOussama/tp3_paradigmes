
liste=[2,7,10,23,27]
def  differences(l):
    m=[]
    for k in range(len(l)-1):
       s=l[k+1]-l[k]
       m.append(s)
    return m 
liste2=differences(liste)
print(liste2)


print("************************")
def itere(L ,n):
    a=[]
    if n==0:
        return L
    elif n==1:
         return differences(L)
    else:
        for i in range(n-1):
            a=differences(L)
            L=a    
        return differences(a)
    
n=int(input("saisir un entier positive: "))        
liste3=itere(liste,n)
print(liste3)