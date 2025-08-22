class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setted = set(nums)
        return len(nums) != len(setted)