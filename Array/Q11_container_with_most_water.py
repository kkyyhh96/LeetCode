#coding:utf-8
# First method
class Solution:
    def maxArea(self, height):
        self.max_area = 0
        for i, h in enumerate(height):
            for j in range(i, len(height)):
                area = self.computeArea(height, i, j) 
                if area > self.max_area:
                    self.max_area = area
        return self.max_area

    def computeArea(self, height, i, j):
        if height[i] > height[j]:
            h = height[j]
        else:
            h = height[i]
        return h * (j - i)

# Second Method
class Solution2:
    def maxArea(self, height):
        self.max_area = 0
        i = 0
        j = len(height) - 1
        while i != j:
            area = self.computeArea(height, i, j)
            if area > self.max_area:
                self.max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -=1
        return self.max_area

    def computeArea(self, height, i, j):
        if height[i] > height[j]:
            h = height[j]
        else:
            h = height[i]
        return h * (j - i)


s = Solution2()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
