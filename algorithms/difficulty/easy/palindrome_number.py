#############
# Author : Yujun Wen
# Last edit: 2022/8/1
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 確認integer是不是回文
解題思路
1.使用[::-1]的操作做反向
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)==str(x)[::-1]:
            return True
        return False
        