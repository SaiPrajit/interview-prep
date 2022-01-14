from ast import List

# Given a fixed-length integer array arr, duplicate each occurrence of zero
# shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not
# written. Do the above modifications to the input array in place and do not return anything.


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if left == length_ - possible_dups:
                    # For this zero we just copy it without duplication.
                    arr[length_] = 0
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]


# Complexity Analysis

# Time Complexity: O(N)O(N), where NN is the number of elements in the array. We do two passes through the array, one to find the number of possible_dups and the other to copy the elements. In the worst case we might be iterating the entire array, when there are less or no zeros in the array.

# Space Complexity: O(1)O(1). We do not use any extra space.
