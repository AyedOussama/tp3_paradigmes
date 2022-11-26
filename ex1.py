
from random import randint;
l=[]
def listAleaInt(n, a, b):
    for i in range(n):
        l.append(randint(a,b))
    return l
l=listAleaInt(5,1,10)
print(l)

a=l.index(min(l))
print(f"l'indice de minimum entier :{l[a]} dans tableau  est {a} ")
print("la liste avant la permutation \n",l)
l[a],l[0]=l[0],l[a]
print("la liste apres la permutation \n",l)
