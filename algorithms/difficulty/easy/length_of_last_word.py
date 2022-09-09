#############
# Author : Yujun Wen
# Last edit: 2022/8/1
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 算出被空格隔開的字串中最後一個字母的長度
解題思路
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split(' ')
        for word in word_list[::-1]:
            if word.isalpha():
                return len(word)
        
        