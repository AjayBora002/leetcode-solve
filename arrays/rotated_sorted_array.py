def bin(nums, target):
    n = len(nums)
    low= 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[high]: # means this part is sorted
            if nums[mid] <= target <= nums[high]:
                low= mid+1
            else:
                high = mid-1
        else:
            if nums[low] <=target<=nums[mid]:
                high = mid-1
            else:
                low = mid + 1
    return -1


def cc(nums, target):
    n=len(nums)
    f=-1
    c=-1
    for i in range(0, n):
        if nums[i] == target:
            if f == -1:

                f=i
            c=i
    if f==-1:
        return 0
    return c-f+1






        




    


        
        












            