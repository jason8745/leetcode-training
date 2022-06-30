#############
# Author : Yujun Wen
# Last edit: 2022/7/1
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number
解題思路
1.很像羅馬字母問題,但這裡不準備mapping來解
TakeAway
- ord會把字母轉成數字
"""
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        n = len(columnTitle)
        for i in range(n):
            result = result * 26
            result += (ord(columnTitle[i]) - ord('A') + 1)
        return result
        
        
        
        