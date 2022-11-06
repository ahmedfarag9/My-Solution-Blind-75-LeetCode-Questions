// Problem 371. Sum of Two Integers
// Given two integers a and b, return the sum of the two integers without using the operators + and -

// Solution using XOR logic operations
// Time Complexity worst case O(n)
// Space Complexity worst case O(n)

// LeetCode Results:
// Runtime: 0 ms, faster than 100.00% of Java online submissions for Sum of Two Integers.
// Memory Usage: 41.2 MB, less than 20.61% of Java online submissions for Sum of Two Integers.

class Solution {
    public int getSum(int a, int b) {

        while (b != 0) {
            int tmp_value = (a & b) << 1;
            a = a ^ b;
            b = tmp_value;
        }
        return a;
    }
}