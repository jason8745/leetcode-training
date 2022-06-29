#############
# Author : Yujun Wen
# Last edit: 2022/6/16
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到List中兩個value相加等於target,即回傳index 
解題思路
1.建立hashmap來記錄value的index
2.每次取得新值就檢查是否找到目標
3.找到後即跳出回圈
TakeAway
- 充分利用hashmap來做到資料index的儲存
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, num in enumerate(nums):
            temp = (target - num)
            if temp in hashmap:
                return[ind,hashmap[temp]]
                break
            hashmap[num]=ind