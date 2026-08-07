class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        min_diff= float('inf')

        for i in range(n):
            left = i + 1
            right = n -1

            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                
                if abs(target - sums)< abs(min_diff):
                    min_diff = target - sums
    

                if sums < target:
                    left += 1
                else:
                    right -= 1
        
        return target - min_diff