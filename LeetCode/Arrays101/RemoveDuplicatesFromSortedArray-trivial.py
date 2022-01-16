# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element
# appears only once. The relative order of the elements should
# be kept the same.

# Constraints
# 0 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # let 's use this as a basis 
        k = 0

        for i in range(len(nums)):
            # detecting duplicate
            if :
                # partition
                nums[k] = nums[i]
                k += 1

        return k