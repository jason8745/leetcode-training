#############
# Author : Yujun Wen
# Last edit: 2022/7/2
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到array中遺失的數字
解題思路
1. sort 完後開始找
2. 要注意不要out of index
TakeAway
- 感覺很多比較,sort後都可以做到
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        
        for i in range(0,len(sorted_list)):
            if sorted_list[i] !=i:
                return i
        return len(nums)
        
        
            
        