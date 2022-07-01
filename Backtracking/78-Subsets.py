'''Leetcode- https://leetcode.com/problems/subsets/'''
'''                   
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

'''
def subsets(nums):
    res = []

    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        #decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        #decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res

#T :O(2^n)
#S :O(n)