class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        min_number = nums[0]
        answer = -1

        for i in range(1, len(nums)):

            if nums[i] > min_number:
               
                answer = max(answer, nums[i] - min_number)
            else:
                min_number = nums[i]


        return answer
