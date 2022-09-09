#############
# Author : Yujun Wen
# Last edit: 2022/7/4
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到交集的元素
解題思路
1.先sort
2. 開始比較
TakeAway
- list.sort() 是一個inplace的方法,使用了會使原本記憶體空間的值,直接sort
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
    
        result = []
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)

        nums1.sort()
        nums2.sort()

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result
        
            
        