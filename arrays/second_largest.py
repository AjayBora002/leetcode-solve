arr=[2,4,1,6,8]
n = max(arr)
x=[i for i in arr if i!=n]
print(max(x))
# TC= O(N)




def s(arr):
    if len(arr)<2:
        return None
    largest=float('-inf')
    sec = float('-inf')
    n=len(arr)
    for i in range(0, n):
        largest=max(arr[i])

    for i in range(0,n):
        if arr[i]>sec and arr[i]!=largest:
            sec=arr[i]
    return sec