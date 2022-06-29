#############
# Author : Yujun Wen
# Last edit: 2022/6/25
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 將兩個Linked List相加成為新的Linked List,過程中若有進位,要帶到next的職
解題思路
1.建立一個result,並且建立指針指向head(但答案不會包含head(0),所以才會是return result.next)
2.建立一個carry來傳遞進位
3.指針操作
TakeAway
- divmod的使用
- 指針的操作複習
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        result_point = result
        carry = 0
        
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry,out = divmod(val1+val2 + carry,10)
            # 指針操作
            result_point.next = ListNode(out) # 確定next的下一步
            result_point = result_point.next # 移動指針
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return result.next
            