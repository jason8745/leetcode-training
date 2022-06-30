#############
# Author : Yujun Wen
# Last edit: 2022/6/30
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 建立pascal's triangle
解題思路
1.看到題型基本上要先聯想到DP
2.第一個和最後一個都為1
3.找出狀態轉移方程: index :j 值為 上一層的index j 和index j-1 相加的值
TakeAway
- Dynamic Programming思考
- 找出狀態轉移方程
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]
            row[0],row[-1]=1,1
            for j in range(1,len(row)-1):
                row[j] = triangle[row_num-1][j-1]+triangle[row_num-1][j]
            
            
            triangle.append(row)
        return triangle
        
        