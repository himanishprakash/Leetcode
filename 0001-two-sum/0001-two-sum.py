class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        dictionary = {}
        result = []

        for i in range(len(nums)):
            dictionary[nums[i]] =  i 


        for i in range(len(nums)):
            sums = target - nums[i]

            if sums in dictionary and i != dictionary[sums]:
                return i, dictionary[sums]