#############
# Author : Yujun Wen
# Last edit: 2022/7/1
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到range中的missing value
解題思路
1.要注意edge case(沒有從lower開始or 沒至upper結尾)
TakeAway
- 邏輯
- 有點難
"""

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def formatRange(lower,upper):
            if lower==upper:
                return str(lower)
            return str(lower)+"->"+str(upper)
        
        result =[]
        prev = lower - 1
        for i in range(len(nums)+1):
            curr = nums[i] if i < len(nums) else upper +1
            # missing value的範圍
            if prev+1 <= curr-1:
                result.append(formatRange(prev+1,curr-1))
            prev = curr
            
        return result
        
        