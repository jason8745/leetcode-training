#############
# Author : Yujun Wen
# Last edit: 2022/6/29
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 用array代表一個數字,回傳+1後的結果(array)
解題思路
1. 從後往前操作,如果是9就變成0,若不是的話就單純+1就結束了
2. 因此若沒有連續需要進位,就可以回傳該時候的答案
3. 如果迴圈跑到完,代表index=0的地方也是9,因為最後要補上1(99-->100)
TakeAway
- 邏輯
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n):
            idx = n-1-i
            if digits[idx]==9:
                digits[idx]=0
            else:
                digits[idx]+=1
                
                return digits
            
        return [1]+digits
            
        