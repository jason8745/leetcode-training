#############
# Author : Yujun Wen
# Last edit: 2022/8/6
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.因為可以有一次的機會跳過,所以如果在主要判斷的程式碼遇到第一次不同,就進入helper函數,如果依然會有不同,就會執行到return
2.如果都沒有觸發helper,代表為回文,就return True
TakeAway
- 雙指標操作
- 回文題目
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s,i,j):
            while i<j:
                if s[i] !=s[j]:
                    return False
                i+=1
                j-=1
            return True
        # 主要判斷程式碼
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return check_palindrome(s,i,j-1) or check_palindrome(s,i+1,j)
            i+=1
            j-=1
        return True
        