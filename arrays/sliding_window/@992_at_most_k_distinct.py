from collections import defaultdict
def distinct(nums, k):
  def at_most(k):  #It calculates the number of subarrays having at most K distinct elements.
    left= 0 
    best = 0
    count = defaultdict(int)
    for right, n in enumerate(nums):
      count[n]+=1
      while len(count)>k:
        count[nums[left]]-=1
        if count[nums[left]] ==0:
          del count[nums[left]]
        left+=1
      best+= right-left+1
    return best
  return at_most(k) - at_most(k-1)

# T.C =O(n)

# exactly k = at most k -at most k-1



# The problem asks:

# Find the number of subarrays containing exactly K distinct integers.

# nums = [1, 2, 1, 2, 3]k = 2



# Subarrays with exactly 2 distinct integers:
# [1, 2]
# [1, 2, 1]
# [1, 2, 1, 2]
# [2, 1]
# [2, 1, 2]
# [1, 2]
# [2, 3]


# Answer = 7.