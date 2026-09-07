#  ums =[3,4,5,1,8,9,2]
# Step 1 : first we will check if i in greater than its next element
#             , if it is, then we will position that element to its right position


# Take 2nd element as a key element , and compare it with its previous element

# if does not satisfies then shift, ifbnot then make the next elememnt --key

nums = [12, 11, 13, 5, 6]
n=len(nums)
for i in range(1,n):
    key=nums[i]  # 2nd emlemt to key bol denge
    j=i-1 # i se pichle wla elemen6t ko j bol denge
    while j>=0 and nums[j]>key :
        nums[j+1] = nums[j]
        j-=1
    nums[j+1] = key
print(nums)




