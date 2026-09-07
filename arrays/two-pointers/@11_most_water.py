def ccontainer(height):
  n= len(height)
  left , right = 0, n-1
  most= 0
  while left<right:
    most = max(most, (right-left) * min(height[left], height[right]))
    if height[left]<height[right]:
      left+=1
    else:
      right-=1
  return most





def most(nums):
  n=  len(nums)
  left, right = 0, n-1
  most = 0
  while left<right:
    most = max(most, (right-left)* min(nums[left], nums[right]))
    if nums[left]<nums[right]:
      left+=1
    else:
      right-=1
      
