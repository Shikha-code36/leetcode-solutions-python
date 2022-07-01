'''Leetcode- https://leetcode.com/problems/permutations-ii/'''
'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
'''

def permuteUnique(nums):
    result = []
    perms = []
    count = {n:0 for n in nums}
    for n in nums:
        count[n] += 1

    def dfs():
        if len(perms) == len(nums):
            result.append(nums.copy())
            return

        for n in count:
            if count[n] > 0:
                perms.append(n)
                count[n]-=1

                dfs()

                count[n] += 1
                perms.pop()

    dfs()
    return result

print(permuteUnique([1,1,2])) #[[1, 1, 2], [1, 1, 2], [1, 1, 2]]

#T:O(n.2^n)
#S:O(n)