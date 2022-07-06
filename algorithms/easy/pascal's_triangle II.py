#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- pascal triangle
解題思路
1.找到狀態轉移方程
2. prev_row = self.getRow(rowIndex-1) 較難
TakeAway
- DP從下往上,Recurrsion從上往下,但都同樣使用了狀態轉移方程
"""
#DP(bottom-up)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex ==0:
            return[1]
        if rowIndex==1:
            return [1,1]
        # 狀態
        prev_row = self.getRow(rowIndex-1)
        new_row = [1 for _ in range(len(prev_row)+1)]
        for i in range(len(prev_row)-1):
            # 狀態轉移方程
            new_row[i+1] = prev_row[i]+prev_row[i+1]
        return new_row