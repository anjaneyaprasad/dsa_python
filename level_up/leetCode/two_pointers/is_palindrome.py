def check_if_palindrome(s):
    """
    "racecar"
    """

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


print(check_if_palindrome("racecar"))

print(check_if_palindrome("abc"))

print(check_if_palindrome("aca"))

print(check_if_palindrome("a"))

print(check_if_palindrome(""))
