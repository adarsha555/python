import math
xmax= float(input("enter xmax:"))
dx= float(input("enter stepsize:"))
r= int(xmax/dx)
x=0
a=[]
b=[]
for i in range(x,r):
    x=x+dx
    f= math.cos(x*(math.pi)/8)
    a.append(x)
    b.append(f)
print ("x:", a)
print ("f(x):",b)