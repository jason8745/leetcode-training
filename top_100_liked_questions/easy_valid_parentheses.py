#############
# Author : Yujun Wen
# Last edit: 2022/6/16
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 檢查字串中,有對應關係的符號(ex: () {})是否左右數量正確,且符合語法順序
解題思路
1.先透過dict儲存符號的對應關係
2.因為符號的合法順序是LIFO,所以這裡可以使用stack
3.stack and i == char_dict[stack[-1]] 是指要同時符合stack不為空,即比對stack最外層
TakeAway
- 如果資料有pair關係,可以透過dict維護
- 如果資料有LIFO特性,可以使用stack
"""
class Solution:
    def isValid(self, s: str) -> bool:
        char_dict={"(":")", "[": "]",  "{": "}"}
        stack=[]
        for i in s:
            if i in char_dict.keys():
                stack.append(i)
            elif stack and  i == char_dict[stack[-1]]:
                stack.pop()
            else:
                return False
                break
            
        return stack==[]