#############
# Author : Yujun Wen
# Last edit: 2022/6/29
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找出平方根
解題思路
1.從2和中間開始做binary search
2.當left<=right時,從兩者中的中點取平方
3.若其中點平方>x,則右邊從中點內縮,若中點平方<x,則左邊從中點前進
TakeAway
- 熟習Binary Search
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2 :
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
            
        return right
            
        