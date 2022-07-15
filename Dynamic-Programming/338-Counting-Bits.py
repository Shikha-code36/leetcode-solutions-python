'''Leetcode- https://leetcode.com/problems/counting-bits/ '''
'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
'''

# Bit manipulation approach
def countBits(self, n):
    ans = []
    for i in range(n+1):
        cur = 0
        while i:
            cur += i & 1
            i >>= 1
        ans.append(cur)
    return ans

# T:O(NlogN)
# S:O(N)

#DP way
def countBits(self, n):
    dp = [0]*(n+1)
    offset = 0

    for i in range(1,n+1):
        if offset*2 == i:
            offset = i
        dp[i] = 1 + dp[i-offset]
    return dp

# T:O(N)
# S:O(N)