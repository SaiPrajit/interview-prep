
# Space Complexity --> O(N)
# Time Complexity --> O(N)
# https://www.youtube.com/watch?v=ih0LW0cuEAk&ab_channel=AlgorithmsMadeEasy

from ast import List


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        pointer = len(nums)-1
        result = [None] * len(nums)

        while left <= right:
            
            if abs(nums[left]) > abs(nums[right]):
                result[pointer] = nums[left]*nums[left]
                left += 1
                pointer -= 1

            else:
                result[pointer] = nums[right] * nums[right]
                right -= 1
                pointer -= 1

        return result
