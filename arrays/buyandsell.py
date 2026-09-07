nums=[1,4,9,2,3]
n = len(nums)
max_profit = 0
min_profit = float('inf')
for i in range (0, n):
    min_profit = min(nums[i], min_profit)
    max_profit = max(nums[i] - min_profit, max_profit)
print(max_profit)



