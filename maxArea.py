def maxArea(self, height):
        result = 0
        temp = 0
        for i, num in enumerate(height):
            for j in range((i+1),len(height)):
                temp = min(num,height[j]) *(j - i)
                if temp > result:
                    result = temp
        return result
