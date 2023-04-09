#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# Efficient Solution
# Time Complexity worst case O(log(n))
# Space Complexity worst case O(1)

# LeetCode Results:
# Runtime: 48 ms, Beats 25.47% of submissions
# Memory Usage: 14.3  MB, less than 11.19% of Python3 online submissions.


from typing import List
import unittest

nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
Output1 = 4

nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
Output2 = -1

nums3 = [1]
target3 = 0
Output3 = -1

nums4 = [1, 3]
target4 = 3
Output4 = 1

nums5 = [3, 5, 1]
target5 = 3
Output5 = 0

nums6 = [4, 5, 6, 7, 0, 1, 2]
target6 = 5
Output6 = 1

nums7 = [8, 9, 2, 3, 4]
target7 = 9
Output7 = 1

nums8 = [4, 5, 6, 7, 8, 1, 2, 3]
target8 = 8
Output8 = 4

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # result = -1

        # if list is empty return -1
        if not nums:
            return -1

        # set right and left elements
        left, right = 0, len(nums) - 1

        while left <= right:
            # set middle point
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid

            # Check if you are in left or right sorted array
            if nums[mid] >= nums[left]:
                # We are in left array
                if target > nums[mid]:
                    # Do binary search on right half
                    left = mid + 1
                elif target < nums[mid]:
                    if target < nums[left]:
                        # Do binary search on right half
                        left = mid + 1
                    elif target >= nums[left]:
                        # Do binary search on left half
                        right = mid - 1

            else:
                # we are in right array
                if target < nums[mid]:
                    # Do binary search on left half
                    right = mid - 1
                elif target > nums[mid]:
                    if target > nums[right]:
                        # Do binary search on left half
                        right = mid - 1
                    elif target <= nums[right]:
                        # Do binary search on right half
                        left = mid + 1

        return -1

# @lc code=end


# Test Cases
class TestSolution(unittest.TestCase):
    def test_search(self):
        Test = Solution()
        self.assertEqual(Test.search(nums1, target1), Output1)
        self.assertEqual(Test.search(nums2, target2), Output2)
        self.assertEqual(Test.search(nums3, target3), Output3)
        self.assertEqual(Test.search(nums4, target4), Output4)
        self.assertEqual(Test.search(nums5, target5), Output5)
        self.assertEqual(Test.search(nums6, target6), Output6)
        self.assertEqual(Test.search(nums7, target7), Output7)
        self.assertEqual(Test.search(nums8, target8), Output8)


if __name__ == "__main__":
    unittest.main()
