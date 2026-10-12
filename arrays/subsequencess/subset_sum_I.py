# identrify the subsets and their sun as a list
# eg.., [5, 3, 2] ist subsets are [5], [3], [2], [5, 3]. [3, 2], [5, 2], [5, 2, 3], []... print their sum in a lst [5, 3,2, 8, 5, 7,10, 0 ]
def subsets(index, total):
  if index>=len(nums):
    r.append(total)
    return 
  sum= total+nums[index]
  subsets(index+1, sum)
  sum = total
  subsets(index+1, sum)


nums = [5, 3, 2]
r = []
subsets(0, 0)

print(r)
