# https://www.youtube.com/watch?v=P1Ic85RarKY&ab_channel=NeetCode
# NO EXTRA MEMORY --> O(1)

from ast import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # m --> index of last value in nums1
        # n --> index of last value in nums2

        # last index of nums1 (not considering 0s)
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]

                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1

            last -= 1

        # edge case
        # fill nums1 with leftover nums2 elements (only they exists
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
