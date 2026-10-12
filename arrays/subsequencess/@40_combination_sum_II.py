def combination(nums, target):
  nums.sort()
  r=[]
  def comb(index, total, sub):
    if total == target:
      r.append(sub[:])
      return
    elif total>target:
      return 
    for i in range(index, len(nums)):
      if i>index and nums[i] == nums[i-1];
        continue
      if total+nums[i]>target:
        break
      sub.append(nums[i])
      sum = total+nums[i]
      comb(i+1, sum, sub)
      sub.pop()
  comb(0, 0, [])
  return r