class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)

        bucket = []
        result = []
        for _ in range(len(nums) + 1):
            bucket.append([])

        for key, value in counts.items():
            bucket[value].append(key)

        for i in range(len(bucket) - 1, 0, -1):

            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return  result


        