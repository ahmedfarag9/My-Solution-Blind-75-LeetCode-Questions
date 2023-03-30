#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# Efficient Solution
# Time Complexity worst case O(n)
# Space Complexity worst case O(1)

# LeetCode Results:
# Runtime: 227 ms, Beats 86.31% of submissions
# Memory Usage: 21.1 MB, less than 89.17% of Python3 online submissions.


from typing import List

nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


if __name__ == "__main__":
    Test = Solution()
    print(Test.productExceptSelf(nums1))
    print(Test.productExceptSelf(nums2))
