class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = length - 1
        change = False
        while i>0:
            if nums[i] > nums[i-1]:
                index = find_nearby(nums, i-1)
                print(nums, i-1, index)
                nums = swap(nums, i, index)
                nums[i:] = nums[i:].reverse()
                break
            i = i-1
        if change == False:
            nums = swap(nums, 0, len(nums)-1)
        return nums

def swap(nums, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t
    return nums

def find_nearby(nums, i):
    min_value = nums[i]
    min_index = i
    for j in range(i+2, len(nums)):
        if nums[j] < min_value and nums[j] > nums[i]:
            min_index = j
            min_value = nums[j]
    return min_index

s = Solution()
print(s.nextPermutation([1,2,3]))
print(s.nextPermutation([3,2,1]))
print(s.nextPermutation([1,1,5]))
print(s.nextPermutation([1,1,5,4,5,1]))
