'''Leetcode- https://leetcode.com/problems/combinations/'''
'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
def combine(n, k):
    result = []

    def backtrack(start,comb):
        if len(comb) == k:
            result.append(comb.copy())
            return

        for i in range(start,n+1):
            comb.append(i)
            backtrack(i+1,comb)
            comb.pop()

    backtrack(1,[])
    return result

#T: O(k.n^k)
#T: O(k. n!/(n-k)!k!)
#S: O(n)