class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        

        minheap = []

        for idx, val in enumerate(nums):
            if len(minheap) < k:
                heappush(minheap, (val, idx))
            else:
                if val > minheap[0][0]:
                    heappop(minheap)
                    heappush(minheap, (val, idx))
            

        ans = []
        minheap.sort(key=lambda x: x[1])
        for val, _ in minheap:
            ans.append(val)
        
        return ans