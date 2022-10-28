
# Solution using Merge sort then searching for adjacent elements
# Time Complexity worst case O(nlog(n))
# LeetCode Runtime Result is around 40 ms

from typing import List


class Solution:

    def mergeSort(self, array: List[int]):

        if len(array) > 1:

            # r is the point where the array is divided into two subarrays
            r = len(array)//2
            L = array[:r]
            M = array[r:]

            # Sort the two halves
            self.mergeSort(L)
            self.mergeSort(M)

            i = j = k = 0

            # Until we reach either end of either L or M, pick larger among
            # elements L and M and place them in the correct position at A[p..r]
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1

            # When we run out of elements in either L or M,
            # pick up the remaining elements and put in A[p..r]
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1

    # Print the array
    def printList(self, array):
        for i in range(len(array)):
            print(array[i], end=" ")
        print()

    # Check for Duplicates

    def containsDuplicate(self, array: List[int]) -> bool:
        for i in range(len(array) - 1):
            if array[i] == array[i+1]:
                return True
        return False


if __name__ == "__main__":

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 15, -5]
    #array = [1, 2, 3, 1]

    Test = Solution()
    Test.mergeSort(array)
