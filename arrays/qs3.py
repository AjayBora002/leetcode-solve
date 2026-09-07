def check(nums):
    """
    Checks if an array 'nums' is a rotated version of a sorted array.
    A sorted and rotated array can have at most one break (drop) in the non-decreasing order.
    """
    count = 0
    n = len(nums)
    
    # Handle the edge case of an array size 0 or 1 (always considered sorted/rotated)
    if n <= 1:
        return True

    # 1. Count drops inside the array
    # Iterate through indices 0 up to n-2
    for i in range(n - 1):
        if nums[i] > nums[i+1]:
            # This is a drop in the non-decreasing order (e.g., 5 followed by 1)
            count += 1
            
    # 2. Check the wrap-around (last vs first element)
    # This accounts for the 'cliff' when the original sorted array was NOT rotated, 
    # or if the rotation point is between the last and first element.
    if nums[n-1] > nums[0]:
        count += 1
        
    # The condition for a sorted and rotated array is that it has 0 or 1 total drops.
    return count <= 1

# --- Example Usage ---
if __name__ == '__main__':
    # True: Sorted [1, 2, 3, 4] rotated 2 times
    print(f"Result for [3, 4, 1, 2]: {check([3, 4, 1, 2])}") # Expected: True (1 drop: 4 > 1)

    # True: Perfectly sorted (0 rotations)
    print(f"Result for [1, 2, 3, 4]: {check([1, 2, 3, 4])}") # Expected: True (1 drop: 4 > 1)

    # False: Two drops, not a rotated sorted array
    print(f"Result for [4, 5, 2, 3, 1]: {check([4, 5, 2, 3, 1])}") # Expected: False (2 drops: 5>2, 3>1)

    # True: Handles duplicates
    print(f"Result for [1, 1, 1, 0, 1]: {check([1, 1, 1, 0, 1])}") # Expected: True (1 drop: 1>0)