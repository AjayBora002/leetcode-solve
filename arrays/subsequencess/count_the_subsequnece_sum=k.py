def subseq(index, total):
  if total == target:
    return 1
  elif total>target:
    return 0
  if index>=len(nums):
    return 0
  sum = total+nums[index]
  pick = subseq(index+1, sum)
  sum = total
  not_pick = subseq(index+1, sum)
  return pick+not_pick
  