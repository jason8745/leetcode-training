#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 很像摘花瓣遊戲
解題思路
1.邏輯
TakeAway
- 邏輯
"""
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n%2==0:
            return True
        else:
            return False