#############
# Author : Yujun Wen
# Last edit: 2022/6/28
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 給定一個n,代表有幾對(),找出合法的所有組合,並列出來
解題思路
1.先列出base case
2.列舉
TakeAway
- 好難~先跳過
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: 
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
        
        