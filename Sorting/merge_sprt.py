def merge(left, right):
    i,j=0,0
    n=len(left)
    m=len(right)
    results = []

    while i<n and j<m:
        if left[i]<right[j]:
            results.append(left[i])
            i+=1
        else:
            results.append(right[j])
            j+=1
    if i<n:
        while i<n:
            results.append(left[i])
            i+=1
    if j<m:
        while j<m:
            results.append(right[j])
            j+=1
    return results

def merge_sort(nums):
    if len(nums)<=1:  # base case as recursion is following
        return nums
    mid = len(nums) // 2
    left_arr=nums[:mid]
    right_arr=nums[mid:]
    l=merge_sort(left_arr)# iska mtlb m baar bar mid nikaalke array ko chota kr dega till single element remain
    r=merge_sort(right_arr)
    return merge(l,r) # last m sinle elements ko sort krke merge kr dega


numbers = [38, 27, 43, 3, 9, 82, 10]
sorted_numbers = merge_sort(numbers)
print("Original:", numbers)
print("Sorted:  ", sorted_numbers)





    