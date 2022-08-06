#############
# Author : Yujun Wen
# Last edit: 2022/8/6
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.先根據unit inplace sort一次List
2.
TakeAway
- dict的資料結構用法
- 另一種sort用法 new_list = sorted(boxTypes,key=lambda x: -x[1]) 兩者都需要用到Lambda函數
- 後續要再研究一下lambda操作
"""
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        cur_size=0
        max_units=0
        for num_box,unit in boxTypes:
            max_units += unit * min(truckSize - cur_size, num_box)
            cur_size += min(truckSize - cur_size, num_box)
        return max_units
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
                
        