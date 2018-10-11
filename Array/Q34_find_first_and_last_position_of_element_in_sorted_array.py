class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        range = [end, -1]
        search(nums, start, end, target, range)
        if range[0] > range[1]:
            range[0] = -1
        return range
        

def search(nums, start, end, target, r):
    mid = int((start + end) / 2)
    if start > end:
        return
    if target == nums[mid]:
        if mid < r[0]:
            r[0] = mid
            search(nums, start, mid-1, target, r)
        if mid > r[1]:
            r[1] = mid
            search(nums, mid+1, end, target, r)
    elif target < nums[mid]:
        search(nums, start, mid-1, target, r)
    else:
        search(nums, mid+1, end, target, r)
           
s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
