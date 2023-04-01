#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# Efficient Solution
# Time Complexity worst case O(log(n))
# Space Complexity worst case O(1)

# LeetCode Results:
# Runtime: 33 ms, Beats 97.32% of submissions
# Memory Usage: 14.2  MB, less than 13.3% of Python3 online submissions.


from typing import List

nums1 = [3, 4, 5, 1, 2]
nums2 = [4, 5, 6, 7, 0, 1, 2]
nums3 = [11, 13, 15, 17]

nums4 = [1]
nums5 = [2, 1]
nums6 = [3, 1, 2]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]

        # set high and low elements
        low, high = 0, len(nums) - 1

        while low <= high:
            # if high value is bigger than low value
            if nums[high] >= nums[low]:
                # array is in original form ( rotated 0 or n times )
                result = min(result, nums[low])
                break

            # else get middle_index element and avoid int overflow
            middle_index = low + (high - low) // 2
            if nums[middle_index] > nums[low]:
                low = middle_index
            elif nums[middle_index] < nums[low]:
                high = middle_index
            else:
                return nums[high]
        return result


if __name__ == "__main__":
    Test = Solution()
    print(Test.findMin(nums1))
    print(Test.findMin(nums2))
    print(Test.findMin(nums3))
    print(Test.findMin(nums4))
    print(Test.findMin(nums5))
    print(Test.findMin(nums6))
