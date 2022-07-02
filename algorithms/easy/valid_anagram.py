#############
# Author : Yujun Wen
# Last edit: 2022/7/2
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 判斷兩個字串是否由相同數量和字母組成
解題思路
1. sort 完後直接比較
TakeAway
- 感覺很多比較,sort後都可以做到
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        return False
        
        
            
        