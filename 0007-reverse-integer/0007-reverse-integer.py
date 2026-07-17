class Solution:
    def reverse(self, x: int) -> int:
        a=x
        x=abs(x)
        s=0  
        while x>0:
          d=x%10
          s=s*10+d
          x=x//10
        if a<0:
            s=-s
        if s<-2**31 or s>2**31-1:
            return 0
        return s
  
