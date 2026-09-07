def rotate(nums, k):
  n =len(nums)
  k = k%10
  def rev(start, end):
    while start<end:
      nums[start], nums[end] = nums[end], nums[start]
      start+=1
      end-=1
  nums.reverse()
  rev(0, k-1)
  rev(k, n-1)