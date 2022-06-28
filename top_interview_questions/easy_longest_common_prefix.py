#############
# Author : Yujun Wen
# Last edit: 2022/6/28
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找出array裡最長的prefix
解題思路
1. 先解決base case
2. 將strs sort 後,只要第一個和最後一個有符合條件,那中間全部都會符合條件,否則就是空字串
TakeAway
- 換個方式思考,下次可以試試
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if len(strs)==1: return strs[0]
        
        strs.sort()
        p=""
        for x,y in zip(strs[0],strs[-1]):
            if x==y:
                p+=x
            else:
                break
        return p
            