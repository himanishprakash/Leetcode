class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        number = {}
        result = []

        for i in range(len(nums)):
            number[nums[i]] = i

        for i in range(len(nums)):

            subs = target - nums[i]

            if subs in number and number[subs] != i:
                return i, number[subs]
            