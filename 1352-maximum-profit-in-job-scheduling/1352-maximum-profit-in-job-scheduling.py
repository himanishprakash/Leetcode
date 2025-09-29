class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        def binary_search(target):
            low, high = 0, n
            
            while low < high:
                mid = (low + high) // 2
                if starts[mid] < target:
                    low = mid + 1
                else:
                    high = mid

            return low
        

        jobs = sorted(zip(startTime,endTime, profit))
        starts = []
        for s, _, _ in jobs:
            starts.append(s)

        n = len(jobs)

        dp = [0] * (n + 1)


        for i in range(n -1, -1, -1):
            s,e,p = jobs[i]
            
            j = binary_search(e)
            dp[i] = max(dp[i + 1], p + dp[j])
            
        
        return dp[0]