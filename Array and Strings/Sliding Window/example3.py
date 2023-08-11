# Example 3: 713. Subarray Product Less Than K. (https://leetcode.com/problems/subarray-product-less-than-k/)

# Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly 
# less than k.

# For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]


def subarraysWithProductLessThanK(nums,k):
    if k<=1:
        return 0
    left = 0
    right = 0
    product = 1
    count = 0
    while right < len(nums):
        product = product * nums[right]
        while product >= k:
            product = product / nums[left]
            left +=1
        count += right - left + 1
        right +=1
    return count


nums = [10, 5, 2, 6]
k = 100
print(subarraysWithProductLessThanK(nums,k))