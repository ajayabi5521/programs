a=[[1,2],
[6,7]]

b=[[1,2],
   [7,8]]


result=[]
for i in range(len(a)):
   output=[]
   for j in range(len(b[0])):
         output.append(a[i][j]*b[i][j])
   result.append(output)      

print(result)          

a=[[2,4,6],
   [5,6,4],
   [3,4,0]]
b=[[5,6,3],
   [9,7,6],
   [4,3,1]]
result=[]
for i in range(len(a)):
   for j in range(len(b[0])):
      output=[]
      for k in range(len(b[0])):
              ans=0
              ans+=a[i][k]*b[k][j]
              output.append(ans)
      result.append(output)
print(result)





from collections import deque

a=[1,2,3,4,5]
d=deque(a)
print(d)

d.append(6)
print(d)

d.popleft()
print(d)

