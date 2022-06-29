#############
# Author : Yujun Wen
# Last edit: 2022/6/26
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找出字串中最長的回文字串長度
解題思路
1.建立輔助程式
2.此輔助程式會找到idx1 到idx2中的符合回文字串的長度
3.使用遞回解法
TakeAway
- 有點難,直接參考了解答,之後再回來看一次
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # base condituin
        if s is '': 
            return s
        max_len = 0 
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandFromCenter(s, i, i)
            len2 = self.expandFromCenter(s, i, i+1)
            l = max(len1, len2)
            # 有點難懂
            if l > end - start:
                start = i - (l - 1) // 2
                end = i + l // 2

        return s[start:end+1]

    def expandFromCenter(self, s, idx1, idx2):
        while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
            idx1 -= 1
            idx2 += 1
        return idx2 - idx1 - 1
        
        
        
        