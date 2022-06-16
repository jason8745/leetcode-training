#############
# Author : Yujun Wen
# Last edit: 2022/6/17
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到一個值插入有序array後的位置
解題思路
1.sorted array--> 使用左、右指標
2.有序array找位址-->使用Binary Search
TakeAway
- 熟悉Binary Search
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            pivot = (left + right) // 2
            if target==nums[pivot]:
                return pivot
            elif target <nums[pivot]:
                right = pivot-1
            else:
                left = pivot+1
        return left