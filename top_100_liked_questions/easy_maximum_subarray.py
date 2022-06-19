#############
# Author : Yujun Wen
# Last edit: 2022/6/19
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 從一個array中,找到連續加總最大的subarray
解題思路
1.所有開頭<0的value皆應拋棄
2.如果累積的subarray<subarray+now_value-->從now_value重新建立subarray
TakeAway
- 未來遇到找最大、最小值的問題時,要直接想到Dynamic Programming
- Kadane's Algorithm
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray =nums[0]
        
        for num in nums[1:]:
            current_subarray = max(num,current_subarray+num)
            max_subarray = max(max_subarray,current_subarray)
            
        return max_subarray