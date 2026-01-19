class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)

        freq = [] 

        for _ in range(len(nums) + 1):
            freq.append([])            
        
        for num, count in counts.items():
            freq[count].append(num)

        result = []

        for i in range(len(freq) - 1, 0 , -1):

            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
