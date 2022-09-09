#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 費式數列
解題思路
1.思考狀態轉移方程
TakeAway
- DP
"""
#iterable
class Solution:
    def fib(self, n: int) -> int:
        if n<=1: return n
        
        current=0
        prev1=1
        prev2=0
        
        for i in range(2,n+1):
            current = prev1+prev2
            prev2=prev1
            prev1=current
        return current

# Recurrsion
class Solution:
    cache = {0: 0, 1: 1}
    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]
        