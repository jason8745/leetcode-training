#############
# Author : Yujun Wen
# Last edit: 2022/7/1
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到happy number
解題思路
1. 很難,直接看了解答,後來發現題目可以轉換思考成,判斷是否有環
2. 判斷是否進入環,可以使用快慢指標來操作,只要有環,快指標一定會追上慢指標
TakeAway
- 
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(number):
            total_sum = 0
            while number>0:
                number,digit = divmod(number,10)
                total_sum +=digit**2
            return total_sum
        
        
        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner !=1 and slow_runner !=fast_runner:
            slow_runner = get_next(slow_runner)  # 走一步
            fast_runner = get_next(get_next(fast_runner)) # 走兩步
        return fast_runner ==1
        
        
            
        