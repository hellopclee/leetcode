class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        size = len(height)
        left = 0
        right = size-1
        while left < right:
            length = right - left 
            if height[left]<= height[right]:
                short = left
                left = left+1
            else:
                short = right
                right = right -1
            water = length*height[short]
            if water > max_water:
                max_water = water

        return max_water
        
