#############
# Author : Yujun Wen
# Last edit: 2022/8/2
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 將數字轉成英文字母
解題思路

TakeAway
- ord的用法
- 也是需要準備一個list
"""
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while columnNumber > 0:
            result.append(capitals[(columnNumber-1)%26])
            columnNumber = (columnNumber-1) // 26
        result.reverse()
        return ''.join(result)
        
        
        