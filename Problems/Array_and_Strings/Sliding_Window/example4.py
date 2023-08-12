# Example 4: Given an integer array nums and an integer k, find the sum of the subarray
# with the largest sum whose length is k.


# Solution
# 1) Loop from 0 to k-1 and get the sum. Store it in largestSum
# 2) Loop from k to len(nums)
#     sum2 = sum2 + nums[i] - nums[i-k]
#     if sum2 < largestSum
#         store sum2 in largestSum


import math


def subArrayWithLargestSumLengthK(nums, k):
    start = 0
    end = 0
    sum2 = 0
    largestSum = -math.inf
    for i in range(0, k):
        sum2 = sum2 + nums[i]
    largestSum = max(sum2, largestSum)
    for i in range(k, len(nums)):
        sum2 = sum2 + nums[i] - nums[i - k]
        largestSum = max(sum2, largestSum)
    return largestSum


nums = [3, -1, 4, 12, -8, 5, 6]
k = 4
# print(subArrayWithLargestSumLengthK(nums, k))
assert subArrayWithLargestSumLengthK(nums, k) == 18, "Failed to run example 4"
