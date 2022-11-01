# Solution using Brute Force Algorithm
# Time Complexity worst case O(n)
# Space Complexity worst case O(n)


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
