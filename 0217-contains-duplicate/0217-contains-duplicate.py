class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        non_dup = set(nums)

        return len(nums) != len(non_dup)