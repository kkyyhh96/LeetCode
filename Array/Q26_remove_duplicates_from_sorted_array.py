class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        result = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[result] = nums[i]
                result += 1
        print(nums)
        return result


s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(s.removeDuplicates([1, 1, 2]))
