#############
# Author : Yujun Wen
# Last edit: 2022/6/29
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 在一以排序好的array中,移除重複值(inplace)
解題思路
1. 利用i,j雙指標,當j指標值和i指標值不同時,就用j指向的值把i取代掉(會是一重複值被取代)
TakeAway
- 邏輯
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                # 取代掉重複值
                nums[i]=nums[j]
        return i+1
            
        