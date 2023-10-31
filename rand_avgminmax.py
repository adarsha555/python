import random
n=int(input("enter n:"))
l=[]
for i in range (n):
    a=random.random()
    l.append(a)


print(l)
print ("MAx:",max(l))
print ("MIN:",min(l))
print ("average:", (sum(l)/n))

