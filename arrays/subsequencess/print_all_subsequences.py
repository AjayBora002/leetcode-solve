# recursive

def sequence(index, subset):
  if index>=len(nums):
    result.append(subset.copy())
    return 
  subset.append(nums[index])
  sequence(index+1, subset)
  subset.pop()
  sequence(index+1, subset)


nums = [1, 2, 3]
result = []

sequence(0, [])

print(result)