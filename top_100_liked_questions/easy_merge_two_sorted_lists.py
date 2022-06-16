#############
# Author : Yujun Wen
# Last edit: 2022/6/17
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 反轉一個Linked List
解題思路
1.從1->2->3->null,變成null<-1<-2<-3,因此只要照原本Linked的順序,但next的方向反過來
TakeAway
- 更熟悉Linked List的操作
- 了解Linked List的reverse操作
- 做reverser可以準備一個temp做暫存
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next # curr的指標指到next_temp
            curr.next = prev # 宣告curr下一步會指到prev
            prev = curr # 將curr當前值放至prev
            curr = next_temp # curr的值為curr的下一步
            
        return prev