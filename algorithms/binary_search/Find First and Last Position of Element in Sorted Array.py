#############
# Author : Yujun Wen
# Last edit: 2022/9/7
# email: yujunwen0517@gmail.com
#####
"""
Note
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        N = len(nums)
        st,end = -1,-1
        l,r = 0,N
        # binary search left
        while l<r:
            mid = (l+r)//2
            if nums[mid]>=target:
                r = mid
            else:
                l = mid+1
        if l<N and nums[l]==target:
            st = l
            
        # binary search right
        l,r = 0,N
        while l<r:
            mid = (l+r)//2
            if nums[mid]<=target:
                l = mid+1
            else:
                r = mid
        if nums[r-1]==target:
            end = r-1
        return [st,end]
        
# time complexity O(logN)
# space complexity O(1)       
