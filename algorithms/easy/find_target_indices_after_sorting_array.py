#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找出target
解題思路
1.先sort後再求解
TakeAway
- 雖然很明顯是二分搜尋法,但還是暴力算完了
"""
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        sorted_arr = sorted(nums)
        for i in range(len(nums)):
            if sorted_arr[i]==target:
                ans.append(i)
        return ans