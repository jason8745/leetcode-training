#############
# Author : Yujun Wen
# Last edit: 2022/8/7
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.
TakeAway
- 
"""
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s==s[::-1]:
            return 1
        return 2
        
