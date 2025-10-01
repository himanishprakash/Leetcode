class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        n = len(stones)

        for i in range(n):
            stones[i] = -stones[i]

        heapify(stones)

        while len(stones) > 1:

            largest_stone = heappop(stones)
            second_largest = heappop(stones)
            if largest_stone != second_largest:
                heappush(stones, largest_stone -second_largest )

        if len(stones) == 1:
            return -heappop(stones)

        else:
            return 0
            