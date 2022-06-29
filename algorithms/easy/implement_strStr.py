#############
# Author : Yujun Wen
# Last edit: 2022/6/29
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 給定兩個字串,若needle出現在haystack,則return 第一個字母出現的index
解題思路
1. 透過迴圈跑haystack去找needle
TakeAway
- 邏輯
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
            
        