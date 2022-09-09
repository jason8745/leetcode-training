#############
# Author : Yujun Wen
# Last edit: 2022/7/2
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 反轉array
解題思路
1.直接reverse
2.直覺是想到這個,但直接s = s[::-1]不給過,要 s[::] = s[::-1]才行,但不知道這樣算不算開了一個新空間?
TakeAway
- 也可以用頭尾雙指標的方式做swap
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[::]=s[::-1]
        
            
        