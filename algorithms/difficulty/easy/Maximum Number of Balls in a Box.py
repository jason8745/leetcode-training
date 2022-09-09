#############
# Author : Yujun Wen
# Last edit: 2022/9/9
# email: yujunwen0517@gmail.com
#####
"""
解題思路
1.建立dict作為box的存放空間
2.取得bit相加(箱子號碼)
3.放入箱子後,和max_count比較
4.最後返回max_count
分析
Time complexity:  O(N*d) , d為highLimit的最大的位數,因為其值有被限制在10的5次方,所以d最大為5
Space complexity: O(N),使用了dict作為儲存 
"""

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = defaultdict(int)
        max_count = float('-inf')
        for num in range(lowLimit,highLimit+1):
            bits = []
            while True:
                # 迴圈次數和highLimit位數有關
                f,m = divmod(num,10)
                bits.append(m)
                num = f
                if f==0:
                    break
            box_num = sum(bits)
            box[box_num]+=1
            max_count = max(max_count,box[box_num])
        return max_count 
        