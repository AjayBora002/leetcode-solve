def fc(nums, target):
    low = 0
    high = len(nums) - 1

    floor = -1
    ceil = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return [target, target]

        elif nums[mid] < target:
            floor = nums[mid]      # possible floor
            low = mid + 1

        else:
            ceil = nums[mid]       # possible ceil
            high = mid - 1

    return [floor, ceil]







            
