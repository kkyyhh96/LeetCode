class Solution:
    def fourSum(self, nums, target):
        two_sum = dict()
        for i, num in enumerate(nums[i: -1]):
            for j, num2 in enumerate(nums[i+1:]):
                sum2 = num + num2
                if sum2 in two_sum:
                    two_sum[sum2].append((i, i+j+1))
                else:
                    two_sum[sum2] = [(i, i+j+1)]

           return result


s = Solution()
print(s.threeSum([1, 0, -1, 0, -2, 2], 0))
#print(s.threeSum([-1, 0, 1, 2, -1, -4]))
#print(s.threeSum([0,0,0,0]))
