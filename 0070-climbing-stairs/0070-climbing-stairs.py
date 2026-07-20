class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def fib(n):
            if n<=1:
               return 1
                
            if dp[n]!=-1:
                return dp[n]
            dp[n]=fib(n-1)+fib(n-2)
            return dp[n]
        return fib(n)
        
        # dp=[-1]*(n+1)
        # dp[0]=1
        # dp[1]=1
        # for i in range(2,n+1):
        #      dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]   
        
 