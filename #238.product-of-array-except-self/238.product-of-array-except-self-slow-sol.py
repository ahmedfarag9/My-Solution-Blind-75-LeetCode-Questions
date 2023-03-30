#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

from typing import List

nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == 0:
                    if j == 0:
                        result.append(1)
                    else:
                        result.append(nums[i])
                else:
                    if i != j:
                        result[j] = result[j] * nums[i]
        return result


if __name__ == "__main__":
    Test = Solution()
    print(Test.productExceptSelf(nums1))
    print(Test.productExceptSelf(nums2))
