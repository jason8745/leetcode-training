#############
# Author : Yujun Wen
# Last edit: 2022/8/6
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.純數學計算
TakeAway
- 不用看答案成功
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2==1 and high%2==1:
            return  2+ ((high-1)-(low+1))//2
        elif low%2==1 or high%2==1:
            return 1+(high-low)//2
        return (high-low)//2
                
        