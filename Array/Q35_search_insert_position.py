class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        return search(nums, start, end, target)
        

def search(nums, start, end, target):
    mid = int((start + end) / 2)
    if start > end:
        return start
    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return search(nums, start, mid-1, target)
    else:
        return search(nums, mid+1, end, target)
           
s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], 0))
