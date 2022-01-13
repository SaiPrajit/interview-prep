from ast import List

# Given a fixed-length integer array arr, duplicate each occurrence of zero
# shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not
# written. Do the above modifications to the input array in place and do not return anything.


class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:
        for index in range(0, len(arr)):
            # shift to the right to open 1 slot            
            if arr[index] == 0:
                

