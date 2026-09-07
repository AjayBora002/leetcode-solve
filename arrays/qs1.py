
# Sample 2:
# Input
# Output
# 5 3
# 7 8 9 1 2
# 9 1 2 7 8
# Explanation:
# rotate 1 step to the right: [2,7,8,9,1]
# rotate 2 steps to the right: [1,2,7,8,9]
# rotate 3 steps to the right: [9,1,2,7,8]


def rotate_left(n,k):
    k=k%len(n)
    return n[k:]+n[:k]
def rotate_right(n,k):
    k=k%len(n)
    return n[-k:]+n[:-k]
x=int(input("enter no of elements : "))
a=[]
for i in range(x):
    n=int(input())
    a.append(n)
k = int(input("Enter value of k (how many rotations): "))
direction = input("Rotate Left or Right? (L/R): ").strip().upper()
if (direction =='L'):
    b=rotate_left(a,k)
    print(b)
elif(direction =='R'):
    c=rotate_right(a,k)
    print(c)

else:
    print("invalid direction")




