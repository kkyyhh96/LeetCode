class Solution:
    def removeElements(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        start = None
        nums.sort()
        end = None
        N = len(nums)
        '''
        if N == 1:
            if nums[0] != val:
                return 0
                '''
        for i, num in enumerate(nums):
            if num == val:
                start = i
                break
        nums.reverse()
        for i, num in enumerate(nums):
            if num == val:
                end = i
                break
        nums.reverse()
        if start != None and end != None:
            nums[start:] = nums[N - end:]
            return len(nums), nums
        else:
            return N

s = Solution()
print(s.removeElements([2, 2, 2], 2))
print(s.removeElements([0,4,4,0,4,4,4,0,2], 4))
print(s.removeElements([0,1,2,2,3,0,4,2], 2))
print(s.removeElements([2], 3))
print(s.removeElements([3, 3], 5))
