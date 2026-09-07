# min and max

def count_non_minimum(nums):
    """
    Calculates the count of elements in 'nums' that are not equal to the minimum value.
    This function uses a procedural (non-OOP) approach.
    """
    # 1. Handle the edge case of an empty list
    if not nums:
        return 0
    
    # 2. Find the minimum element in the list
    # The built-in min() function is very efficient (O(N) time complexity).
    minimum = min(nums)
    
    # 3. Count how many times the minimum element appears
    # The built-in count() method is also efficient (O(N) time complexity).
    count_min = nums.count(minimum)
    
    # 4. Calculate the result
    # Total elements - (Count of minimum elements) = (Count of non-minimum elements)
    return len(nums) - count_min

# --- Execution Logic (Non-OOP Main Block) ---
if __name__ == '__main__':
    # Example 1: Standard case
    test_nums_1 = [3, 1, 4, 1, 5, 9, 2]
    result_1 = count_non_minimum(test_nums_1)
    
    print(f"List: {test_nums_1}")
    print(f"Minimum Value: {min(test_nums_1)}")
    print(f"Count of Non-Minimum Elements: {result_1}\n") # Expected: 7 - 2 = 5

    # Example 2: List where the minimum appears once
    test_nums_2 = [10, 20, 5, 30]
    result_2 = count_non_minimum(test_nums_2)
    
    print(f"List: {test_nums_2}")
    print(f"Minimum Value: {min(test_nums_2)}")
    print(f"Count of Non-Minimum Elements: {result_2}") # Expected: 4 - 1 = 3