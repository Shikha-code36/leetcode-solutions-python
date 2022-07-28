'''Leetcode - https://leetcode.com/problems/two-sum/ '''
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''

# Solution1
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
# T:O(N^2)
# S:O(1)

# Solution2 
def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in dict:
            return [dict[diff], i]
        dict[nums[i]] = i

# T: O(N)
# S: O(N)


