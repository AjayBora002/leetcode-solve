def subsequence(index, total, subset):
  if total == target:
    result.append(subset.copy())
    return 
  elif total>target:
    return 
  if index>=len(nums):
    return
  subset.append(nums[index])
  sum = total+nums[index]
  subsequence(index+1, sum, subset)
  e = subset.pop()
  sum-=e
  subsequence(index+1, sum, subset)



nums = [2, 3, 5, 7]
target = 10
result = []

subsequence(0, 0, [])

print(result)