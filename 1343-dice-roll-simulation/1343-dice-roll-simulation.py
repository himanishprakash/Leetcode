class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        BIG = 10**9 + 7

        dp = [[0]*7 for _ in range(n+1)]
        for k in range(6):
            dp[1][k] = 1
        dp[1][-1] = 6
        dp[0][-1] = 1 # FIX, see below, this way the "rollMax" correction
                      #      is correct for f==0

        for r in range(2, n+1):
            for k in range(6):
                dp[r][k] = dp[r-1][-1]
                if r > rollMax[k]:
        
                    f = r-rollMax[k]-1
                    dp[r][k] -= (dp[f][-1] - dp[f][k])

                dp[r][-1] += dp[r][k]

            dp[r][-1] %= BIG

        return dp[n][-1]