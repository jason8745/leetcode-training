#############
# Author : Yujun Wen
# Last edit: 2022/9/9
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.透過count儲存次數,candidate儲存候選digit
2.當達到count==3時,就判斷如果比候選digit大就更新候選digit
分析
Time complexity:  O(N) , 使用了一個迴圈
Space complexity: O(1),只使用了count和candidate做儲存
"""

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count = 1
        candidate = ""
        for i in range(1,len(num)):
            if num[i-1]==num[i]:
                count+=1
            else:
                count = 1
            if count==3:
                candidate= max(candidate,num[i])
        return candidate*3 
        