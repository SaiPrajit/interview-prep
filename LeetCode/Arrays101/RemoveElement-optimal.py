# https://www.youtube.com/watch?v=Pcd1ii9P9ZI&ab_channel=NeetCode
# k --> number of values that are not val
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            # performing the swap (not really because we erase 2)
            if nums[i] != val:
                # partition
                nums[k] = nums[i]
                k += 1

        return k
