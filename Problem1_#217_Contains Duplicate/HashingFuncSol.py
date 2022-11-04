# Problem 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Solution using Hash Function
# Time Complexity worst case O(n)
# Space Complexity worst case O(n)

# LeetCode Results:
# Runtime: 1090 ms, faster than 41.85% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26 MB, less than 27.65% of Python3 online submissions for Contains Duplicate.

from typing import List

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 15, -5]


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create Hash set
        hash_set = set()

        # Check if set contains input list elements
        for i in nums:
            if i in hash_set:
                return True
            hash_set.add(i)
        return False


if __name__ == "__main__":
    Test = Solution()
    print(Test.containsDuplicate(test))
