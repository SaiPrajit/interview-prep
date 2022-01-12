# O(N)

from typing import List


class Solution:
    def findMaxConsecutiveOnes1(self, nums: List[int]) -> int:
        maxHere, theMax = 0, 0
        for num in nums:
            theMax = max(theMax, maxHere=num == 0 ? 0: maxHere+1)
