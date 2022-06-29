#############
# Author : Yujun Wen
# Last edit: 2022/6/29
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 合併兩個array後並sort
解題思路
1.先把nums2塞進去後sort
TakeAway
- 邏輯
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(n):
            nums1[i+m]=nums2[i]
            
        nums1.sort()
                    
        
        
            
        