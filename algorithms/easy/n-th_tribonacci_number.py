#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- tribonacci
解題思路
1.同費式數列的思考方式
TakeAway
- 儲存空間可以再優化
"""
class Solution:
    cache = {0: 0, 1: 1,2 : 1}
    def tribonacci(self, n: int) -> int:
        
        
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2)+self.tribonacci(n - 3)
        return self.cache[n]