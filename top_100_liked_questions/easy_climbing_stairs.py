#############
# Author : Yujun Wen
# Last edit: 2022/6/21
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 爬樓梯問題
解題思路
1.爬樓梯問題為Dynamic Programming,會有重疊子問題,可以透過備忘錄來極大幅度減少子問題
TakeAway
- 爬樓梯問題為Dynamic Programming 
- 透過備忘錄來減少重疊子問題
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp={} # 備忘錄,暫存計算結果
        if n==1:
            return 1
        dp[1]=1
        dp[2]=2
        i = 3
        while i<=n:
            dp[i]=dp[i-1]+dp[i-2]
            i+=1
        
        return dp[n]
            
        

        