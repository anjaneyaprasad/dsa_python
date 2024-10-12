def helper(s1, s2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if s1[m - 1] == s2[n - 1]:
        return helper(s1, s2, m - 1, n - 1)
    else:
        return 1 + min(helper(s1, s2, m, n - 1),
                       helper(s1, s2, m - 1, n),
                       helper(s1, s2, m - 1, n - 1))


def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    return helper(s1, s2, m, n)

# s1 = "CAT"
# s2 = "CUT"
# print(edit_distance(s1, s2))


# s1 = "CAT"
# s2 = ""
# print(edit_distance(s1, s2))


# s2 = "CAT"
# s1 = ""
# print(edit_distance(s1, s2))


s1 = "SUNDAY"
s2 = "SATURDAY"
print(edit_distance(s1, s2))
