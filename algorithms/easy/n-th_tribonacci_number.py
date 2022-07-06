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
    cache = {0: 0, 1: 1,2 : 1}
    def tribonacci(self, n: int) -> int:
        
        
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2)+self.tribonacci(n - 3)
        return self.cache[n]