def bin(nums):
    n = len(nums)
    low= 0
    high = n-1
    while low<high:
        mid = (low+high)//2
        
        if nums[mid] < nums[high]:
            high = mid
        else:
            low=mid+1
    return nums[low] 













# nums = [4,4,5,6,1,2,3,3]
