class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        answer = {}

        for i in range(len(nums)):
            answer[nums[i]] = i

        
        for j in range(len(nums)):

            comp = target - nums[j]
            
            if comp in answer and answer[comp] != j:
                
                return j, answer[comp]