def consecutiive(nums):
  n = len(nums)
  c= 0 
  max_c = 0
  for i in range(0, n):
    if nums[i] == 1:
      c+=1
      max_c = max(max_c, c)
    else:
      c= 0 
  return max_c







