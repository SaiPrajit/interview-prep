from typing import List

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted
# in non-decreasing order.
# Squaring each element and sorting the new array is very trivial
# could you find an O(n) solution using a different approach?

# O(N*log(N))


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums[i] *= nums[i]

        nums.sort()
        return nums
