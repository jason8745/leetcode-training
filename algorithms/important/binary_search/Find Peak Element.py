#############
# Author : Yujun Wen
# Last edit: 2022/9/7
# email: yujunwen0517@gmail.com
#####
"""
Note
透過BS快速找到沒有升序排列的值
Time complexity O(logN)
Space complexity O(1)   
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                # 這一步比較關鍵
                r = mid
        return l
        
     
