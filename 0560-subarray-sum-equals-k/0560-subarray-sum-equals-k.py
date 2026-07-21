class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        prefix_sum_dict = {0:1}

        prefix_sum = 0
        count = 0

        for i in nums:
            prefix_sum += i

            if prefix_sum - k in prefix_sum_dict:
                count += prefix_sum_dict[prefix_sum - k]


            if prefix_sum in prefix_sum_dict:
                prefix_sum_dict[prefix_sum] += 1
            else:
                prefix_sum_dict[prefix_sum] = 1


        return count
        