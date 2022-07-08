'''Leetcode- https://leetcode.com/problems/combination-sum-iii/'''
'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
'''


def combinationSum3(k, n):
    res = []

    def backtrack(cur, n, start):
        if k == len(cur):
            if n == 0:
                res.append(cur.copy())
            return
        for i in range(start, 10):
            cur.append(i)
            backtrack(cur, n-i, i+1)
            cur.pop()
    backtrack([], n, 1)
    return res
