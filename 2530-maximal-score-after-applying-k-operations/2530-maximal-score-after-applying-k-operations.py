class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]

        nums.sort()
        sums = 0
        for _ in range(k):
            max_element = heapq.heappop(nums)
            sums += (-1) * max_element
            heapq.heappush(nums,max_element // 3)

        return sums


            


        


