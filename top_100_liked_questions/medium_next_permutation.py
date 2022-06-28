#############
# Author : Yujun Wen
# Last edit: 2022/6/28
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找出array的下一個排列組合
解題思路
1.首先從底部往左開始,當nums[i-1]<nums[i]就停在i
2.找到後換從i開始,往右找直到nums[j]<=nums[i-1]停止
3.找到後就swap
TakeAway
- 好難~先跳過
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i-1 >=0 and nums[i-1]>=nums[i]:
            i-=1
            
        if i-1>=0:
            j = i
            while j<len(nums) and nums[j]>nums[i-1]:
                j+=1
            # swap
            nums[i-1],nums[j-1] = nums[j-1],nums[i-1]

        m = i
        n = len(nums)-1
        
        while m<n:
            nums[m],nums[n] = nums[n],nums[m]
            m+=1
            n-=1