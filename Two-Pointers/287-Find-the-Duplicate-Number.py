"Leetcode- https://leetcode.com/problems/find-the-duplicate-number/ "
'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
'''

# Solution-1
def findDuplicate(self, nums):
    nums.sort()

    for i in range(len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

# T:O(nlogn)
# S:O(n)

# Solution-2- using set
def findDuplicate(self, nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

# T:O(n)
# S:O(n)

# Solution-3- Binary Search
def findDuplicate(self, nums):
    # 'low' and 'high' represent the range of values of the target
    low = 1
    high = len(nums) - 1

    while low <= high:
        cur = (low + high) // 2
        count = 0

        # Count how many numbers are less than or equal to 'cur'
        count = sum(num <= cur for num in nums)
        if count > cur:
            duplicate = cur
            high = cur - 1
        else:
            low = cur + 1

    return duplicate

# T:O(nlogn)
# S:O(1)

# Solution-4- Two Pointers Floyd's Tortoise and Hare (Cycle Detection)
def findDuplicate(self, nums):
     # Find the intersection point of the two runners.
    to = hr = nums[0]
    while True:
        to = nums[to]
        hr = nums[nums[hr]]
        if to == hr:
            break
        
    # Find the "entrance" to the cycle.
    to = nums[0]
    while to != hr:
        to = nums[to]
        hr = nums[hr]
        
    return hr
    
# T:O(n)
# S:O(1)
