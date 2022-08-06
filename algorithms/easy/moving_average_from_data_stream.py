#############
# Author : Yujun Wen
# Last edit: 2022/8/6
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.純邏輯
TakeAway
- 不用看答案成功
- del的用法
"""
class MovingAverage:

    def __init__(self, size: int):
        self.list=[]
        self.size=size
        

    def next(self, val: int) -> float:
        if len(self.list)<self.size:
            self.list.append(val)
        else:
            del self.list[0]
            self.list.append(val)
            
        return sum(self.list)/len(self.list)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
                
        