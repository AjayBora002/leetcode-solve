def remove(nums):
    if not nums:
        return 0
    j=1
    for i in range (1, len(nums)):
        if nums[i]!=nums[i-1]:
            nums[j] = nums[i]
            j+=1
    del nums[j:]
    return j
    
arr = [1, 1, 2, 2, 3, 4, 4]
length = remove(arr)
print(arr)

#Tc=O(1)










arr = [1, 1, 2, 2, 3, 4, 4, 5]
unique_arr = list(dict.fromkeys(arr))

print(unique_arr)
# Output: [1, 2, 3, 4, 5]


