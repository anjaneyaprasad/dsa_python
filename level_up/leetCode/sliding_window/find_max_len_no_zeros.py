"""
You are given a binary string s (a string containing only "0" and "1").
You may choose up to one "0" and flip it to a "1".

What is the length of the longest substring achievable that contains only "1"?
"""

arr = "1101100111"


def find_length(arr):
    n = len(arr)
    if 0 == n:
        return n

    left = curr = ans = 0

    for right in range(n):
        if arr[right] == "0":
            curr += 1
        while curr > 1:
            if arr[left] == "0":
                curr -= 1
            left += 1
        if curr == 1:
            ans = max(ans, right - left + 1)

    return ans


print(find_length("1101100111"))
print(find_length("1111100111"))
print(find_length(""))
print(find_length("0"))
print(find_length("00"))
print(find_length("101"))
