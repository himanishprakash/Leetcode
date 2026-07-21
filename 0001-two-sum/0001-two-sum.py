class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = {}

        for i in range(len(nums)):
            dictionary[nums[i]] = i

        result = []
        for i in range(len(nums)):

            subs = target - nums[i]

            if subs in dictionary and i != dictionary[subs]:
                return i, dictionary[subs]

        