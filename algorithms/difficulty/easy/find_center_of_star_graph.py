#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找圖的中點
解題思路
1.既然有保證代表兩個連線的交點一定是中點
TakeAway
- 
"""
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return(set(edges[0]) & set(edges[1])).pop()
        
        