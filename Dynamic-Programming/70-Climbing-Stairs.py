'''Leetcode- https://leetcode.com/problems/climbing-stairs/ '''
'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''
#Top down TLE #T:O(2^n)
def climbStairs(n):
    if n==1:
        return 1
    if n==2:
        return 2

    return climbStairs(n-1)+climbStairs(n-1)

#Top down + memorization (list)
def climbStairs(self,n):
    if n == 1:
        return 1
    arr = [-1 for i in range(n)]
    arr[0], arr[1] = 1, 2
    return self.helper(n-1, arr)

def helper(self, n, arr):
    if arr[n] < 0:
        arr[n] = self.helper(n-1, arr)+self.helper(n-2, arr)
    return arr[n]

# Top down + memorization (dictionary/hashmap) #TLE
def climbStairs(n):
    dic = {1:1,2:2}
    if n not in dic:
        dic[n] = climbStairs(n-1)+climbStairs(n-2)
    return dic[n]

# Bottom up, O(n) space
def climbStairs(n):
    if n==1:
        return 1
    res = [0 for i in range(n)]
    res[0],res[1] = 1,2

    for i in range(2,n):
        res[i] = res[i-1] + res [i-2]
    return res[-1]

# Bottom up, constant space
def climbStairs(n):
    one,two = 1,1

    for i in range(n-1):
        temp = one
        one = one+two
        two = temp
    return one

#T:O(n)
