from collections import deque

def sliding_window_max(nums, k):
    q = deque()
    result = []

    for i in range(len(nums)):

        # remove out of window
        if q and q[0] < i - k + 1:
            q.popleft()

        # maintain decreasing order
        while q and nums[q[-1]] < nums[i]:
            q.pop()

        q.append(i)

        if i >= k - 1:
            result.append(nums[q[0]])

    return result