def two_sum_subarray(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return False
    
    window_sum = 0
    max_sum = float('-inf')

    for i in range(len(nums)):
        window_sum += nums[i]

        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[i - (k - 1)]

    return max_sum