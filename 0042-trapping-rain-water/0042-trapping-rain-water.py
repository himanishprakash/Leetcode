class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height) 
        left = 0
        right = n - 1
        left_sum = height[left]
        right_sum = height[right]

        trapped = 0
        while left < right:

            if left_sum < right_sum:
                left += 1
                left_sum = max(height[left], left_sum)
                trapped += max(0, left_sum - height[left])

            else:
                right -= 1
                right_sum = max(right_sum, height[right])
                trapped += max(0,right_sum - height[right] )

        return trapped