from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        consecMax = consec

        for num in nums:
            if num == 1:

                consec = consec + 1

                if consec > consecMax:
                    consecMax = consec

            elif num == 0:
                consec = 0

        return consecMax