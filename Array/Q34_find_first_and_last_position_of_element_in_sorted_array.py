class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        return search(nums, start, end, target)
        

def search(nums, start, end, target):
    mid = int(start + end) / 2

    if nums[mid] == target:
        return [mid, mid]
    if start > end:
        return [-1, -1]
    if nums[start] >= target and num[end] <= target:
        search(nums, start, mid-1, target)
        search(nums, mid+1, end, target)
           
s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
