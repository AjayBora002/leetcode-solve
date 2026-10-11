# a single element can be picked unlimited time
def combination(nums, target):
  r=[]
  def sums(index, total, subset):
    if total == target:
      r.append(subset.copy())
      return 
    elif total>target:
      return 
    if index > len(nums):
      return 
    subset.append(nums[index])
    sum = total+nums[index]
    sums(index, sum, subset) # not index+1 because we want to choose that element again
    sum =total
    subset.pop()
    sums(index+1, sum, subset)
  sums(0, 0, [])
  return r
