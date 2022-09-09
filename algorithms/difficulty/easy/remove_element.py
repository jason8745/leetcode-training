#############
# Author : Yujun Wen
# Last edit: 2022/8/1
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- removeElement
解題思路
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[count]=nums[i]
                count+=1
        return count
        