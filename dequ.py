
from collections import deque

a=['ajay','abi','raja','Rajesh']
d=deque(a)
print(d)

    from collections import deque

a=['ajay','abi','raja','Rajesh']
d=deque(a)
print(d)
name=input("enter name:")
d.append(name)
print(d)
       

for i in d:
    d.popleft()
    print(d)
    name=input("Enter your name:")
    d.append(name)


