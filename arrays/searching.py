n=int(input())
arr=[]
for i in range (n):
    x=int(input())
    arr.append(x)
    
e=int(input())
if e in arr:
    print("YES")
else:
    print("NO")