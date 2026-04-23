class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        n = len(nums)
        
        left_sum = [0] * n
        right_sum = [0] * n
        result = [0] * n


        left_sum[0] = 1
        for i in range(1,n):
            left_sum[i] = left_sum[i - 1] * nums[i -1]

        right_sum[n - 1] = 1

        for i in range(n -1, 0,-1):
            right_sum [i - 1] = right_sum[i] *  nums[i]
        

        for i in range(n):
            result[i] = right_sum[i] * left_sum[i]

      
        return result
