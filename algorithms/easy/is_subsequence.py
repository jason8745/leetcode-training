#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 檢查s是否為t的subsequence
解題思路
1.在subsequence走到底之前(其中一個指標走到bound)
2. 如果p_left走到底(left_bound),代表s是t的subsequence
TakeAway
- 雙指標
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_bound, right_bound = len(s), len(t)
        
        p_left = p_right=0
        while p_left < left_bound and p_right <right_bound:
            if s[p_left]==t[p_right]:
                p_left+=1
            p_right+=1
            
        return p_left==left_bound
        
        