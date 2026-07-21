class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diction = {}

        for i in range(len(nums)):
            diction[nums[i]] = i

        for i in range(len(nums)):

            subs = target - nums[i]
            if subs in diction and i != diction[subs]:
                return i,diction[subs]
