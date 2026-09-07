def maxi(nums):
    n=len(nums)
    curr_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, n):
        curr_sum = max(nums[i], curr_sum+nums[i])
        max_sum = max(curr_sum, max_sum)
    return max_sum



# --- Driver Code (Test Cases) ---
if __name__ == "__main__":
    # Test Case 1: Standard example with mixed numbers
    test_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Test 1: {test_1}")
    print(f"Max Sum: {maxi(test_1)}\n")







