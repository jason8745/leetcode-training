#############
# Author : Yujun Wen
# Last edit: 2022/6/27
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 從array中找出三個數相加為0的所有組合,並且三個元素皆不重複
解題思路
1.先對array做排序
2.排序過後,如果該數大於零,後面的數也都會比他大,無法找到組合,可以直接跳出迴圈
3.若當前值與前一個值相同,也跳過(元素不可以重複)
4.使用輔助函數 twoSum
5. twoSum中使用雙指標lo,hi
6.因為答案需要求的是threeSum,因此將第一個數固定(所以lo才會是i+1)
7.透過找到後面兩個數(相加==nums[i],且三者不重複),就是我們要的組合
TakeAway
- 將數先排序後,想法會比較直觀
- 將問題做轉換的思維(將實際是three的問題轉為了以前學習過的twoSum)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i==0 or nums[i-1]!=nums[i]:
                self.twoSum(nums,i,res)
        return res
    
    
    def twoSum(self,nums:List,i:int,res:List):
        lo,hi = i+1,len(nums)-1
        while (lo<hi):
            sum = nums[i]+nums[lo]+nums[hi]
            if sum < 0:
                lo+=1
            elif sum >0:
                hi -=1
            else:
                res.append([nums[i],nums[lo],nums[hi]])
                lo+=1
                hi-=1
                while lo<hi and nums[lo]==nums[lo-1]:
                    lo+=1
        
        
        
        