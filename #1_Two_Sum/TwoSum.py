# Problem 1. Two Sum
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Solution using Hash Function
# Time Complexity worst case O(n)
# Space Complexity worst case O(n)

# LeetCode Results:
# Runtime: 129 ms, faster than 61.56% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 53.89% of Python3 online submissions for Two Sum.

from typing import List

# Test Cases
nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3, 2, 4]
target2 = 6

nums3 = [3, 3]
target3 = 6


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create Hash set
        new_dict = {}
        # Check if set contains input list elements
        for i in range(len(nums)):
            v = target - nums[i]
            if v in new_dict:
                return [new_dict[v], i]
            new_dict[nums[i]] = i
        return []


if __name__ == "__main__":
    Test = Solution()
    print(Test.twoSum(nums1, target1))
    print(Test.twoSum(nums2, target2))
    print(Test.twoSum(nums3, target3))
