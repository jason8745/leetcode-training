#############
# Author : Yujun Wen
# Last edit: 2022/8/6
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.透過dict來記錄timestamp時間
TakeAway
- 不用看答案成功
"""
class Logger:

    def __init__(self):
        self.limit={}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.limit.keys():
            self.limit[message]=timestamp
            return True
        else:
            if self.limit[message]+10>timestamp:
                return False
            else:
                self.limit[message]=timestamp
                return True
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
                
        