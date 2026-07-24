class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left = 0
        right = n - 1
        right_sum = height[right]
        left_sum = height[left]

        result = 0
        while left < right:

            if left_sum < right_sum:
                left += 1
                left_sum = max(left_sum, height[left] )
                result += max(0, left_sum - height[left])

            else:
                right -= 1
                right_sum = max(right_sum, height[right])
                result += max(0, right_sum - height[right])

        return result
