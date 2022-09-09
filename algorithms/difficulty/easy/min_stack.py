#############
# Author : Yujun Wen
# Last edit: 2022/6/24
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 實作一個stack
解題思路
1.一開始直接用min來取得最小值有點偷吃步,所以回來看,如果不用此方法該如何解
2.重點是pop時,若最後一個元素相同,則要同步處理,否則取最小值會取到被pop出的值
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val<= self.min[-1]:
            self.min.append(val)
        

    def pop(self) -> None:
        if self.min[-1]==self.stack[-1]:
            self.min.pop()
        self.stack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]