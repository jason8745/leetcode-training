#############
# Author : Yujun Wen
# Last edit: 2022/7/2
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 如果array裡有重複的值就return True
解題思路
1. 利用python 的set
TakeAway
- 總算覺得有一題很簡單的了
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums))!=len(nums):
            return True
        return False
        
        
            
        