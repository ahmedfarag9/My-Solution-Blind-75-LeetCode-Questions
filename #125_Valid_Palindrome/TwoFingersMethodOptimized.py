# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the same
# forward and backward. Alphanumeric characters include letters and numbers.
#
#  Given a string s, return true if it is a palindrome, or false otherwise.
#
#
#  Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
#  Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
#  Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
#
#  Constraints:
#
#
#  1 <= s.length <= 2 * 10⁵
#  s consists only of printable ASCII characters.
#
#
#  Related Topics Two Pointers String 👍 5763 👎 6499
#
#
# Solution using  Two Pointers method Optimized
# Time Complexity worst case O(n)
# Space Complexity worst case O(1)

# LeetCode Results:
# Runtime: 52 ms Beats 45.79% of submissions
# Memory Usage: 14.6 MB, Beats 95.61% submissions.

# leetcode submit region begin(Prohibit modification and deletion)

# Define the input strings
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

# Define the Solution class with method isPalindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two Pointers solution / Using two pointers, one at the start and one at the end for memory efficiency
        left, right = 0, len(s) - 1
        while left < right:
            # Skip non-alphanumeric characters from both ends
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare the lowercase versions of the remaining characters
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

        # Check the results by calling the isPalindrome function on each string
if __name__ == "__main__":
    Test = Solution()
    print(Test.isPalindrome(s1))  # Output: True
    print(Test.isPalindrome(s2))  # Output: False
    print(Test.isPalindrome(s3))  # Output: True
