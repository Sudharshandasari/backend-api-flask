def min_window_substring(s, t):
    from collections import Counter

    need = Counter(t)
    window = {}

    have = 0
    need_count = len(need)

    res = [-1, -1]
    res_len = float("inf")

    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            have += 1

        while have == need_count:
            # update result
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # shrink
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1

            left += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else "" 