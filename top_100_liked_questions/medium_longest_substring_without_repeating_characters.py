#############
# Author : Yujun Wen
# Last edit: 2022/6/26
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 從字串中找出沒有重複的最長的子字串
解題思路
1.建立一個sub來存放子字串答案
2.一有重複的string,就更新sub 字串,使其從下一個index重新開始累積
TakeAway
- 思考練習
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        sub=''
        for char in s:
            if char not in sub:
                sub += char
                ans = max(ans,len(sub))
            else:
                
                cut = sub.index(char)
                sub = sub[cut+1:]+char
        return ans
        
        
        
        