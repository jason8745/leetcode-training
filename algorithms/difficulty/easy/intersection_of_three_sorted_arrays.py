#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到三個arr都有的值並排序寫出
解題思路
1.利用Set來做這件事
TakeAway
- list 不能用&比較,因此可以先轉成set
"""
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(list(set(arr1) & set(arr2) &set(arr3)))
        
        