#############
# Author : Yujun Wen
# Last edit: 2022/6/27
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 給定一個數字字串,其有對應的英文(ex:lookup),找出其包含的英文字母的所有排列組合(長度==len(數字字串))
解題思路
1.準備一個lookup
2.根據輸入的number,將字母(list)放進letter_lists中
3.len(letter_litst)>1,代表輸入的數字至少>=2,可以開始做排列組合
4.把list pop出來後開始運算
TakeAway
- 這題好像純考想不想的到怎麼解
- pop完
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        # if input is 23 then letter_lists will like
        # [["a","b","c"],["d","e","f"]]
        letter_lists = []
        for ch in digits:
            letter_lists.append(lookup[ch])
            
        while len(letter_lists)>1:
            l1 = letter_lists.pop()
            l2 = letter_lists.pop()
            combos = []
            for i in l1:
                for j in l2:
                    combos.append(j+i)
            letter_lists.append(combos)
            
        return [] if not letter_lists else letter_lists[0]
            