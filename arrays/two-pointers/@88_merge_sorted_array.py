def merge(nums1, nums2, m, n):
  m = len(nums1)
  n= len(nums2)
  i = m-1
  j = n-1
  k = m+n-1
  while j>=0:
    if i>=0 and nums1[i]>nums2[j]:
      nums1[k] = nums1[i]
      i-=1
    else:
      nums1[k] = nums1[j]
      j-=1
    k-=1
    