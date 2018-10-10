class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        return bi_search(nums, start, end, target)

def bi_search(nums, i, j, target):
    mid = int((i + j) / 2)
    if i > j:
        return -1
    if nums[mid] == target:
        return mid
    if nums[i] <= nums[mid]: 
        if nums[i] <= target and nums[mid] >= target:
            return bi_search(nums, i, mid-1, target)
        else:
            return bi_search(nums, mid+1, j, target)
    else:
        if nums[j] >= target and nums[mid] <= target:
            return bi_search(nums, mid+1, j, target)
        else:
            return bi_search(nums, i, mid-1, target)
            
s = Solution()
print(s.search([4,5,6,7,0,1,2], 3))
print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([5, 1, 3], 5))
