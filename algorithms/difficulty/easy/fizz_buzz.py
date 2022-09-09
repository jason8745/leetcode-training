#############
# Author : Yujun Wen
# Last edit: 2022/7/4
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- fizz_buzz問題
解題思路
1.直接暴力解了
TakeAway
- 
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        num_list = list(range(1,n+1))
        for ind,v in enumerate(num_list):
            if v%3==0:
                if v%5==0:
                    num_list[ind]="FizzBuzz"
                else:
                    num_list[ind]="Fizz"
            elif v%5==0:
                if v%3==0:
                    num_list[ind]="FizzBuzz"
                else:
                    num_list[ind]="Buzz"
            else:
                num_list[ind]=str(v)
        return num_list
        
            
        