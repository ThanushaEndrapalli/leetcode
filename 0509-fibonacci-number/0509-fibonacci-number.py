class Solution:
    def fib(self, n: int) -> int:
        
        dp=[-1]*(n+1)
        def fib(n,dp):
            if n<=1:
                dp[n]=n
                return dp[n]
            if dp[n]!=-1:
                return dp[n]
            dp[n]=fib(n-1,dp)+fib(n-2,dp)
            return dp[n]
        
        return (fib(n,dp)) 