"Leetcode- https://leetcode.com/problems/squares-of-a-sorted-array/ "
'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''

# Solution 1
def sortedSquares(self, nums):
    ans = []

    for i in range(len(nums)):
        ans.append(nums[i]*nums[i])
        i += 1

        ans.sort()
    return ans

#T: O(NLOGN)
#S: O(N)

# Solution 2 - Two Pointer
def sortedSquares(self, nums):
    i = 0
    j = len(nums)-1
    temp = []
    while(i <= j):
        if nums[i]*nums[i] > nums[j]*nums[j]:
            temp.append(nums[i]*nums[i])
            i += 1
        else:
            temp.append(nums[j]*nums[j])
            j -= 1
    return temp.sort()

#T: O(N)
#S: O(N)
