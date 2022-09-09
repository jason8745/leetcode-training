#############
# Author : Yujun Wen
# Last edit: 2022/7/1
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- reverse一個32 bit後,以10進位呈現
解題思路
1. 感覺這個操作很特別,先跳過
TakeAway
- 
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0,31
        while n:
            ret+=(n & 1 ) <<power
            n = n >> 1
            power-= 1 
        return ret
        
        
            
        