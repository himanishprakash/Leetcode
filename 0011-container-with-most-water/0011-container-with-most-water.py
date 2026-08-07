class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        right = len(height) - 1
        left = 0

        max_volume = 0 

        while left < right:

            width = right - left

            max_volume = max(max_volume, width * min(height[left], height[right]))

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_volume



