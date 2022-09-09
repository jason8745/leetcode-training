#############
# Author : Yujun Wen
# Last edit: 2022/8/6
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.若相同指標就同時前進
2.遇到非法就return False
3.若遇到數字,就新增一個指標來做比較
4.最後比較雙指標是否有成功走到終點來判斷
TakeAway
- 指標操作
"""
class Solution:
    def validWordAbbreviation(self, word, abbr):
        i = j = 0
        m, n = len(word), len(abbr)
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            # 最難的區塊
            elif abbr[j].isnumeric():
                k = j
                while k < n and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        return i == m and j == n
        