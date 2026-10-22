def combination(n, k):  # k= no of slements in the subset should be
  r = []
  def subsequence(index, total, subset):
    if len(subset) == k:
      if total == n:
        r.append(subset[:])
      return 
    if index >= 9 or total >n:
      return 
    subset.append(index+1)
    subsequence(index+1, total+index+1, subset)
    subset.pop()
    subsequence(index+1, total, subset)
  subsequence(0, 0, [])
  return r
