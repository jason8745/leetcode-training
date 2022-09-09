#############
# Author : Yujun Wen
# Last edit: 2022/7/4
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到第一個沒有重複元素的值並回傳其index
解題思路
1.用了兩個hashtable,一個存出現次數,一個存出現的位置
2. 找到出現次數==1(不重複),出現次數hashtable找到其位子
TakeAway
- 使用hashtable
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        ind = {}
        for i, ch in enumerate(s):
            if ch not in ind:
                ind[ch]=i
            if ch not in count:
                count[ch]=1
            else:
                count[ch]+=1
                
        for k,v in count.items():
            if v==1:
                return ind[k]
        return -1
        
            
        