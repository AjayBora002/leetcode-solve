def is_sorted(nums):
    n = len(nums)
    # Iterate up to the second to last element
    for i in range(0, n - 1):
        # If current element is bigger than the next, it's not sorted
        if nums[i] > nums[i+1]:
            return False
            
    return True

# Test cases
print(is_sorted([1, 2, 3, 4, 5]))  # Output: True
print(is_sorted([1, 5, 3, 4, 9]))  # Output: False





