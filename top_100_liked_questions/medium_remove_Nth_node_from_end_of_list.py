#############
# Author : Yujun Wen
# Last edit: 2022/6/27
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 給定一個head(指向Linked List),移除從後面數來第N個元素後,回傳整個List
解題思路
1.Linked List 是無法像array 一樣透過index直接刪除元素的
2.找到該元素後,只要將指標指向next.next,跨過該元素,其實就是跳過他指向下一個,就可以達到目的了
3.當size>n+1時 p 開始移動,這樣在cur指到None值時,p就會指到從後面數來第N個元素
4.當size==n時,代表該數為最前面的那個值,因此return head.next(head原本指向的值是要被skip掉的)
5.若size!=n時,跨過他(next.next),並回傳head
TakeAway
- 指標只能從頭開始操作
- 學會在Linked List中如何找到從後面數來第N個的元素
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 1
        cur = p = head
        # 直到cur跑到底(指向None之前)
        while cur.next:
            size+=1
            cur = cur.next
            if size > n+1:
                p = p.next
        
        if size==n:
            return head.next
        else:
            p.next = p.next.next
            return head
            