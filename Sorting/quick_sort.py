# array h usme ek pivot point le lo, can take any element , but generally 1st for easir understanding
#Step 2: el left index h ek right index h , dono ko ek ek loop variable diya
# left se aage jao aur aesa element dhundo jo pivot se bdaa ho
#right se piche aao aur aesa element dundho jo pivogt se chota ho
# i aur j ki value mili, ab inhe swap krdo,and go on
# ek baar i, j overlap jab honge tum dekhoge pivot se chote element are on left and bigger elemnet are on right 
#after this swap pivot with j  , ab pivot beech m h

def partition(nums, low , high):
    pivot=nums[low]
    i=low
    j=high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick(nums, low, high):
    if low<high:
        pi=partition(nums, low , high)
        quick(nums, low, pi-1)
        quick(nums, pi+1, high)


data = [10, 7, 8, 9, 1, 5]
quick(data, 0, len(data) - 1)
print("Sorted Array:", data)







# choos emiddle element as pivot
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x<=pivot]
    right = [x for x in arr[1:] if x>pivot]
    return quicksort(left) + [pivot] + quicksort(right)

arr = [10, 7, 8, 9, 1, 5]
a=quicksort(arr)
print("Sorted Array:", a)




def quick(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[len(arr) //2]
    left = [x for x in arr[1:] if x<=pivot]
    middle = [x for x in arr[1:] if x==pivot]
    right = [x for x in arr[1:] if x>pivot]
    return quick(left) +[pivot] +quick(right)



