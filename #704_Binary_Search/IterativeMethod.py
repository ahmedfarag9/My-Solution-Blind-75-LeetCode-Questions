# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Solution using Binary Search Iterative Method
# Time Complexity worst case O(log(n))
# Space Complexity worst case O(1)

# LeetCode Results
# Runtime: 661 ms, faster than 19.62% of Python3 online submissions for Binary Search.
# Memory Usage: 15.5 MB, less than 73.99% of Python3 online submissions for Binary Search.

from typing import List

# Test Cases
nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
result1 = 4

nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
result2 = -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if list is empty return false
        if len(nums) == 0:
            return -1

        # if list is 1 element check it
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1

        # if list is 2 elements check them
        if len(nums) == 2:
            if target == nums[0]:
                return 0
            elif target == nums[1]:
                return 1
            return -1

        # if list is 2 elements check them
        if len(nums) > 2:
            low = 0
            high = len(nums) - 1

        # Repeat until pointers high and low meet
        while low <= high:
            # Get mid element and avoid int overflow
            mid = low + (high - low) // 2

            # Compare mid to target
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        # Return -1 if target not found
        return -1


if __name__ == "__main__":
    Tests = Solution()
    if result1 == Tests.search(nums1, target1):
        print("nums1 = [-1,0,3,5,9,12] | target1 = 9 | result1 = 4")
        print("Test 1 passed, found target: " + str(target1) + " at index:" + str(result1))
    else:
        print("Test 1 failed")

    if result2 == Tests.search(nums2, target2):
        print("nums2 = [-1,0,3,5,9,12] | target2 = 2 | result2 = -1")
        print("Test 2 passed, didn't find target:" + str(target2))
    else:
        print("Test 2 failed")
