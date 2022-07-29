"Leetcode- https://leetcode.com/problems/subarray-product-less-than-k/ "
'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
'''

# Solution-1 TLE
def numSubarrayProductLessThanK(self, nums, k):
    count = 0
    ans = 1
    for i in range(0, len(nums)):
        if nums[i] < k:
            count += 1
        ans = nums[i]
        for j in range(i+1, len(nums)):
            ans = ans*nums[j]

            if ans < k:
                count += 1
            else:
                break
    return count

# T:O(N^2)
# S:O(1)

# Solution-2
def numSubarrayProductLessThanK(self, nums, k):
    if k <= 1:
        return 0
    prod = 1
    cur = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        cur += right - left + 1
    return cur

# T:O(N)
# S:O(1)