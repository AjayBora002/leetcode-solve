from collections import defaultdict
def distinct(nums, k):
  def at_most(k):
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
