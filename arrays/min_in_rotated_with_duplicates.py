def bin(nums):
    n=len(nums)
    low = 0
    high= n-1
    while low<high:
        mid = (low+high)//2
        if nums[mid] < nums[high]:
            high = mid
        elif nums[mid] > nums[high]:
            low = mid+1
        else:
            high = high-1
    return nums[low]











