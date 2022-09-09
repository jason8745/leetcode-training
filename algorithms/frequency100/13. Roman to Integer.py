#############
# Author : Yujun Wen
# Last edit: 2022/9/10
# email: yujunwen0517@gmail.com
#####
"""
Note
1.需要處理減的Case
Time complexity: O(1),因為有所限制 finite set
Space complexity: O(1)   
"""



class Solution:
    def romanToInt(self, s: str) -> int:
        values={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total

