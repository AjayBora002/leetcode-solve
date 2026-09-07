def remove(nums):
  n=len(nums)
  slow  =0 
  for fast in range(n):
    if slow<2 and nums[fast] != nums[slow-2]:
      nums[slow] =  nums[fast]
      slow+=1
  return slow