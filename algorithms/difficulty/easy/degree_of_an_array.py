#############
# Author : Yujun Wen
# Last edit: 2022/8/8
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.有點難,之後再回來看
2.
TakeAway
- 之後可以透過difaultdict先設定初始值,就不用再去考慮沒有值的問題了
"""
class Solution:
    def findShortestSubArray(self, nums):
        # 先透過dict計算出degree
        nums_map, deg, min_len = collections.defaultdict(list), 0, float('inf')
        for index, num in enumerate(nums):
            nums_map[num].append(index)
            deg = max(deg, len(nums_map[num]))
        for num, indices in nums_map.items():
            if len(indices) == deg:
                min_len = min(min_len, indices[-1] - indices[0] + 1)
        return min_len
        



                
        