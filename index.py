#To find the symmetric difference of two sets
M=int(input("set1 : "))
a=set()
for i in range(0,M):
  x=int(input(end=""))
  a.add(x)

N=int(input("set2 : "))
b=set()
for i in range(0,M):
  y=int(input(end=""))
  b.add(y)

z=set()
z=((a|b)-(a&b))

for i in z:
    print(i)