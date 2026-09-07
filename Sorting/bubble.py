def bubble(nums):
    n=len(nums)
    for i in range (0,n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

nums = list(map(int, input().split()))

bubble(nums)
print(nums)



# for best case

def bubble(nums):
    n=len(nums)
    for i in range (0,n):
        swapped=False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if not swapped:
            break
nums = list(map(int, input().split()))

bubble(nums)
print(nums)
 # now its TC is O(N)

