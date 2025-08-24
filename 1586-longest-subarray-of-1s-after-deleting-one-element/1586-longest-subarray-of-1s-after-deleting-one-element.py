class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left = 0
        longest = 0
        num_zeroes = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                num_zeroes += 1

            while num_zeroes > 1:
                if nums[left] == 0:
                    num_zeroes -= 1

                left += 1

            longest = max(longest, right - left)


        return longest