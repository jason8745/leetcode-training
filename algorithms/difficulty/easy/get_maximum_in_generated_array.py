#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- Get Maximum in Generated Array
解題思路
1.有點難,但看的出來是DP
2. 
TakeAway
- DP
"""
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0: 
            return 0
        
        arr=[0,1] #base array
        for i in range(2, n+1):
            # 狀態轉移方程
            if i%2==0:
                arr.append(arr[i//2])
            else:
                arr.append(arr[i//2] + arr[i//2 + 1])
        return max(arr)
        
        