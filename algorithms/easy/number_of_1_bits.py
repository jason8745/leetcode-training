#############
# Author : Yujun Wen
# Last edit: 2022/7/1
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 求hammingWeight
解題思路
1. bit操作
TakeAway
- 
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n>0:
            if n & 1:
                ans+=1
            n  >>=1
        return ans
        
        
            
        