class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        else:
            self.set = set()
            result = []
            dic = {}
            old = []
            nums = sorted(nums)
            for i, num1 in enumerate(nums):
                if i >= 1 and nums[i] == nums[i - 1]:
                    continue
                else:
                    for j in range(i+1, len(nums) - 1):
                        num2 = nums[j]
                        num3 = -(num1 + nums[j])
                        if num3 in nums[j+1:]:
                            dic[(num1, num2)] = num3
            for key, value in dic.items():
                result.append([key[0], key[1], value])
            return result


s = Solution()
print(s.threeSum([-1, -2, 1, 2]))
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0,0,0,0]))
