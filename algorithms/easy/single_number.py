#############
# Author : Yujun Wen
# Last edit: 2022/6/24
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找出array裡單獨出現的元素
解題思路
1.用一個array紀錄資料,然後對整個目標array跑迴圈尋找
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_arr =[] 
        for i in nums:
            if i not in single_arr:
                single_arr.append(i)
            else:
                single_arr.remove(i)
        return single_arr[0]
        