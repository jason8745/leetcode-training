#############
# Author : Yujun Wen
# Last edit: 2022/6/28
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 羅馬數字轉換
解題思路
1. 從左邊開始,如果該數非最後一個數(i+1<len(s)),且該數下一個數大於他,代表此為減的符號,直接處理兩個數,然後走兩步
2. 若非減例則直接放入即可
TakeAway
- 邏輯
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        values={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total
        