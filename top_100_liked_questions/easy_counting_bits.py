#############
# Author : Yujun Wen
# Last edit: 2022/6/25
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 有點難理解(先跳過)
解題思路
1.DP+ Last Set bit(這個不太懂)
TakeAway
- DP的概念,要找出那個方程式
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for x in range(1,n+1):
            # DP方程式
            ans[x] = ans[x&(x-1)]+1
        return ans
        
        