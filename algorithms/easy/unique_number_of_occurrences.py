#############
# Author : Yujun Wen
# Last edit: 2022/8/6
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.先把所有出現的數字存到dict中,並同時記錄出現次數
2.再判斷出現次數是否有重複(使用set)
TakeAway
- 不用看答案成功
- dict的資料結構用法
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count={}
        for n in arr:
            if n not in count.keys():
                count[n]=1
            else:
                count[n]+=1
        return True if len(set(count.values()))==len(count.values()) else False
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
                
        