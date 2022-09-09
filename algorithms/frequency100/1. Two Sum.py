#############
# Author : Yujun Wen
# Last edit: 2022/9/10
# email: yujunwen0517@gmail.com
#####
"""
Note
Time complexity: O(N)
Space complexity: O(N)   
"""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, num in enumerate(nums):
            temp = (target - num)
            if temp in hashmap:
                return[ind,hashmap[temp]]
                break
            hashmap[num]=ind

