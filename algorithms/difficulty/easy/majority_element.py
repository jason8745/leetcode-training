#############
# Author : Yujun Wen
# Last edit: 2022/6/24
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 從一個list找出最常出現的元素
解題思路
1.利用HashMap儲存次數,待出現超過n/2時即回傳該數
TakeAway
- HashMap使用
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for n in nums:
            if n not in hash_map:
                hash_map[n]=1
            else:
                hash_map[n]+=1
            if hash_map[n]>len(nums)/2:
                return n
                