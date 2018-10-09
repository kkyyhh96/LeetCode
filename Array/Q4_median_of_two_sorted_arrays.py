class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        if l % 2 != 0:
            return nums[int(l/2)]
        else:
            return (nums[int(l / 2)]+ nums[int(l / 2 -1)])/2



s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))
print(s.findMedianSortedArrays([1, 2, 5], [3, 4]))
