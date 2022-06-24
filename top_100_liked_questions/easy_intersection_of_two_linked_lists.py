#############
# Author : Yujun Wen
# Last edit: 2022/6/24
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到一個Linked List插入另一個Linked 的那個節點
解題思路
1.先把其中一條linked list 節點加到一個set中
2.如果發現Linked List有資料在裡面,則回傳該node
TakeAway
- Linked List的操作複習
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_in_B = set()

        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next

        while headA is not None:
            if headA in nodes_in_B:
                return headA
            headA = headA.next

        return None
        