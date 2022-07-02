#############
# Author : Yujun Wen
# Last edit: 2022/7/2
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到3的次方
解題思路
1.邏輯
TakeAway
- 
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n ==0:
            return False
        if n==1:
            return True      
        while n >1 :
            a,b = divmod(n,3)
            if  b !=0:
                return False
            if a == 1:
                return True
            n = a
        
        
            
        