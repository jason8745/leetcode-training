#############
# Author : Yujun Wen
# Last edit: 2022/6/30
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 將句子只保留字母後,判斷是否為迴文
解題思路
1.判斷迴文可以思考雙指標,從兩端開始比較
2.因為沒有先處理掉非字母,因此遇到非字母就前進
TakeAway
- 回文題型
- 雙指針操作
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
    
        while left < right:
            # 非字母不列入判斷
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # 不合條件提早跳出
            if left < right and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
    
        return True
        
        