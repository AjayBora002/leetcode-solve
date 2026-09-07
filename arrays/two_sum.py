def two(nums, target):
  f={}
  n = len(nums)
  for i in range(0, n):
    diff = target - nums[i]
    if diff in f:
      return [f[diff], i]
    f[nums[i]] = i