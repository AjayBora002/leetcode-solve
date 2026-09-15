def soo(nums):
    n = len(nums)
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums








def sor(nums):
    n=  len(nums)
    l = 0
    m = 0
    h = n-1
    while m<=h:
        if nums[m] == 0:
          nums[m], nums[l] = nums[l], nums[m]
          l+=1
          m+=1
        elif nums[m] == 1:
          m+=1
        else:
            nums[m], nums[h]  = nums[h], nums[m]
            h-=1
    return nums
        
          
        