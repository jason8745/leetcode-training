#############
# Author : Yujun Wen
# Last edit: 2022/6/25
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 將array中的0全部趕到最後面,要求in-place修改,不另外開空間
解題思路
1.透過python list的操作
TakeAway
- python list操作
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num ==0:
                nums.remove(num)
                nums.append(num)