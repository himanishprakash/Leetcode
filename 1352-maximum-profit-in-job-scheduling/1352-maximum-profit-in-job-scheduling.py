class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        def binary_search(target):
            low, high = 0 ,n

            while low < high:
                mid = (low + high) // 2

                if starts[mid] < target: 
                    low = mid + 1
                else:
                    high = mid

            return low

        jobs = sorted(zip(startTime,endTime,profit))
        n = len(jobs)
        dp = [0] * (n + 1)

        starts = []

        for s, _ , _ in jobs: 
            starts.append(s)

        for i in range(n -1, -1, -1):
            start, end , profit = jobs[i]
            j = binary_search(end)
            dp[i] = max(dp[i + 1], profit + dp[j])


        return dp[0]
