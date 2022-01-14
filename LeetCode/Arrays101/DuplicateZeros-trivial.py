from ast import List

# Given a fixed-length integer array arr, duplicate each occurrence of zero
# shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not
# written. Do the above modifications to the input array in place and do not return anything.


class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:

        numExtraSpace = 0
        # creating a new array with the necessary extra space
        for index in range(0, len(arr)):
            # shift to the right to open 1 slot
            if arr[index] == 0:
                numExtraSpace += 1

        newList = [None] * (len(arr) + numExtraSpace)

        index = 0

        # alocatting space using the correct configuration
        while index < len(newList):
            newList[index] = arr[index]

            if newList[index] == 0:
                newList[index+1] = 0
                index += 1

        arr = newList
