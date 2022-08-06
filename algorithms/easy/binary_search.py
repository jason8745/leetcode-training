#############
# Author : Yujun Wen
# Last edit: 2022/8/6
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.二元搜尋經典
2.因為會遇到只有一個數,所以需要i<=j
TakeAway
- 竟然可以完全不看答案寫出來了!!!!
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums== None:
            return -1
        i=0
        j=len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                i=mid+1
            elif nums[mid]>target:
                j=mid-1
        return -1
                
        