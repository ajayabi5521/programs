def printd(s):
    for i in s:
        print(i)
s="happy birthday"

        
def add(*a):
    print(a)
add('ajay','bala','raj',23,25)

def gread(**a):
    print(a["age"])
gread(name="bala",age=34,place="kkl")


def add(a,b):
    return a+b
print(add(2,add(5,6)))
result=add(5,6)
print(result)
