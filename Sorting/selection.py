# ex....nums=[1,4,2,6,3,9]
#Step 1: first it will set 1 as minimum index, then with the i+1 intex it will compare i 
# Step 2: if min_index is greater move to next element 
# Step 3: if not , then set the compared number to min_index
# Step 4: now compare that new min_index to all the next elements
# Step 5 : after comparing will all , we have got our minimum number
# Step 6: we will swap the minimum number with the i index number
# Step 7: then the loops value increeases with 1 and same thing repeats

def selection(nums):
    n=len(nums)
    for i in range (0, n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]



nums = list(map(int, input().split()))
selection(nums)
print(nums)



