def majority(nums):
  candidate = 0
  count = 0
  for num in nums:
    if count ==0:
      candidate = num
    count+=1 if num==candidate else -1 # if num equals current element it increments by 1 else decrement by 1
  return candidate




# TC = O(N), SC = O(1)




# using hash map
