nums = [1,3,-2,-4,5,-9]
n =len(nums)
result = [0]*n
pos , neg = 0, 1
for i in range(0, n):
    if nums[i] < 0:
        result[neg] = nums[i]
        neg+=2
    else:
        result[pos] = nums[i]
        pos+=2
print(result)




