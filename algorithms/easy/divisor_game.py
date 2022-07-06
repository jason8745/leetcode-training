#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 詭異題
解題思路
1.思考狀態轉移方程
TakeAway
- DP
"""
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n%2==0:
            return True
        else:
            return False