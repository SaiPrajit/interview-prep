# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Only one valid answer exists.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        processed_number_dict = dict()
        for a in range(len(nums)):
            if (target-nums[a]) in processed_number_dict.keys():
                return([a, processed_number_dict[target-nums[a]]])
            else:
                processed_number_dict[nums[a]] = a
