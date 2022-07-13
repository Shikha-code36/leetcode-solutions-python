'''Leetcode -https://leetcode.com/problems/maximum-subarray/'''
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
'''

# Solution1
import math

def maxSubArray(nums):
    max_s = -math.inf
    for i in range(len(nums)):
        currentS = 0
        for j in range(i, len(nums)):
            currentS += nums[j]
            max_s = max(max_s, currentS)
    return max_s

# T:O(N^2)
# S:O(1)

# Solution2
def maxSubArray(nums):
    max_sum = cur_sum = float('-inf')

    for i in nums:
        cur_sum = max(cur_sum + i, i)
        max_sum = max(max_sum, cur_sum)

    return max_sum
# T:O(N)
# S:O(1)
