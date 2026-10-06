def subsequence(index, total, subset):
  if total == k:
    result.append(subset.copy())
    return True
  elif total>k:
    return False
  if index >= len(nums):
    return False
  subset.append(nums[index])
  sum = total+nums[index]
  pick =subsequence(index+1, sum, subset)
  if pick == True:
    return True
  e = subset.pop()
  sum=  total
  not_pick= subsequence(index+1, sum, subset)
  return not_pick