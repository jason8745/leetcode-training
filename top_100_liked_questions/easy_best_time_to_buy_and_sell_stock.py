#############
# Author : Yujun Wen
# Last edit: 2022/6/24
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 給定一個array代表股價,想辦法買低賣高
解題思路
1.概念跟求最大連續合很相似
2.試圖買到最低點,只要開頭不是最低點都不會是我們想要的解
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price = prices[i]
            elif prices[i]-min_price >max_profit:
                max_profit = prices[i]-min_price
        return max_profit