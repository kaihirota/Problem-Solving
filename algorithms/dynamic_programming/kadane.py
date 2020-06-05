def max_subarray(nums):
    """Find the largest sum of any contiguous subarray."""
    current_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        current_max = max(nums[i], nums[i] + current_max)
        global_max = max(global_max, current_max)
    return global_max


assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
