# Example 2: You are given a binary string s (a string containing only "0" and "1").
# You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?
# For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.


s = "1101100111"


def longestSubstringOfOne(s):
    start = 0
    L = list(s)
    count = 0
    end = 0
    flag = 0
    length = 0
    while end < len(L):
        if L[end] == "0":
            count += 1
        while count > 1:
            if L[start] == "0":
                count -= 1
            start += 1
        length = max(end - start + 1, length)
        end += 1
    return length


# print(longestSubstringOfOne(s))
assert longestSubstringOfOne(s) == 5, "Failed to run example 2"
