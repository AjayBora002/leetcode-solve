def three(nums, target):
  nums.sort()
  n = len(nums)
  ans = nums[0]+nums[1]+nums[2]
  for i in range(n-2):
    l = i+1
    r = n-1
    while l<r:
      total= nums[i]+nums[l]+nums[r]
      if total == target:
        return total
      if abs(total-target) < (ans-target):
        ans = total
      if total<target:
        l+=1
      else:
        r-=1
  return ans




