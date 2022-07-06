#############
# Author : Yujun Wen
# Last edit: 2022/7/6
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到最小成本
解題思路
1.找到狀態轉移方程
TakeAway
- DP從下往上,Recurrsion從上往下,但都同樣使用了狀態轉移方程
"""
#DP(bottom-up)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minimum_cost =[0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            take_one_step = minimum_cost[i-1]+cost[i-1]
            take_two_step = minimum_cost[i-2]+cost[i-2]
            # 狀態轉移方程
            minimum_cost[i] = min(take_one_step,take_two_step)
            
        return minimum_cost[-1]

# recurrsion(top-down)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minimum_cost(i):
            # Base case, we are allowed to start at either step 0 or step 1
            if i <= 1:
                return 0

            # Check if we have already calculated minimum_cost(i)
            if i in memo:
                return memo[i]

            # If not, cache the result in our hash map and return it
            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            memo[i] = min(down_one, down_two)
            return memo[i]

        memo = {}
        return minimum_cost(len(cost))