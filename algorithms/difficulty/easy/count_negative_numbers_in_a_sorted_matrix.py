#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找m*n中,小於0的值數量,竟量讓方法符合O(m+n)
解題思路
1.因為column 和row都有符合遞減,因此當row一遇到小於0時,其後的值都會<0
2.因此這邊反著數回去
TakeAway
- 
"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, cnt = m - 1, 0, 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                cnt += n - c
                r -= 1
            else:
                c += 1
        return cnt