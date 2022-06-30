'''
                                Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''


def permute(nums):
    result = []

    # base case
    if len(nums) == 1:
        return [nums.copy()] #ornums[:] is a deep copy

    for i in range(len(nums)):
        n = nums.pop()
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result

#T:O(2^n)
#S:O(n)
