#############
# Author : Yujun Wen
# Last edit: 2022/9/10
# email: yujunwen0517@gmail.com
#####
"""
Note
最難的限制是Time complexity需要O(log(M+N))內,否則沒有此限制,可以直接merge後取median
之後要再看一次
Time complexity: O(log(min(M,N))) 
Space complexity O(1) 
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+len(nums2)
        half = total//2
        
        if len(nums2)<len(nums1):
            nums1,nums2 = nums2,nums1
            
        left = 0
        right = len(nums1)-1
        while True:
            nums1_mid = (left+right)//2
            nums2_mid = half-nums1_mid-2
            # 交叉比對,確認分段是否正確
            nums1_start = nums1[nums1_mid] if nums1_mid >=0 else float('-inf')
            nums1_next = nums1[nums1_mid+1] if nums1_mid+1<len(nums1) else float('inf')
            nums2_start = nums2[nums2_mid] if nums2_mid>=0 else float('-inf')
            nums2_next = nums2[nums2_mid+1] if nums2_mid+1<len(nums2) else float('inf')
            if nums1_start <= nums2_next and nums2_start <=nums1_next:
                if total%2==0:
                    return(max(nums1_start,nums2_start)+min(nums1_next,nums2_next))/2
                return min(nums1_next,nums2_next)
            elif nums2_start>nums1_next:
                left = nums1_mid+1
            else:
                right = nums1_mid-1
                

