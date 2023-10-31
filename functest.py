import random
x = random.randint(1,6)
n=0
while x != 6:
    n = n+1
    x = random.randint(1,6)
    print (x)

print("it took",n ," throws to get a 6")