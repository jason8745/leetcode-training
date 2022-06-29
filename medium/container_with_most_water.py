#############
# Author : Yujun Wen
# Last edit: 2022/6/26
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找出最大裝水的容量area
解題思路
1.主要利用左右雙指標的方式來求解
2.為了使水不漏出,因此高度為左右兩邊最低的那個值
3.逐漸往內收(從最大寬度開始找答案)
4.更新時選擇替換掉較矮的邊
TakeAway
- 需要邏輯清晰
- 利用左右雙指標
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height)-1
        while left<right:
            width = right-left
            maxarea = max(maxarea,min(height[left],height[right])*width)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return maxarea
        
        
        
        