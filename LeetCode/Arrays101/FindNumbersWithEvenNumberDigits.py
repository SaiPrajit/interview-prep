
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        numEvenDigits = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                numEvenDigits += 1

        return numEvenDigits
