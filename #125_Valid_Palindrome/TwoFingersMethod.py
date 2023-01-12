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
# Solution using  Two Pointers method
# Time Complexity worst case O(n)
# Space Complexity worst case O(n)

# LeetCode Results:
# Runtime: 46 ms, Beats 87.89% of submissions
# Memory Usage: 15 MB, less than 34.46% of Python3 online submissions for Two Sum.

# leetcode submit region begin(Prohibit modification and deletion)

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "
class Solution:
    class Solution:
        def isPalindrome(self, s: str) -> bool:
            # Remove all characters and spaces except alpha-numeric
            result = "".join(c for c in s if c.isalnum())

            # Lower case all characters
            result = result.lower()

            # Two Pointers solution
            start, end = 0, len(result) - 1
            while start < end:
                if result[start] == result[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True

if __name__ == "__main__":
    Test = Solution()
    print(Test.isPalindrome(s1))
    print(Test.isPalindrome(s2))
    print(Test.isPalindrome(s3))

