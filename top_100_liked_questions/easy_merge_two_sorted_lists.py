#############
# Author : Yujun Wen
# Last edit: 2022/6/16
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 將兩個Linked List由小到大排序
解題思路
1.先理解Linked List的資料結構(值、指標)和指標移動機制(python原生是沒有這個資料結構的)
2.此解總共有三個指標(List1指標、List2指標、prehead指標)
3.經比較後,該條List的值若較小,則該List指標前進,並將prev指標指向該list,直到任意Linked List為空,則最後一步則指到非空
TakeAway
- 了解Linked List的指標機制
- Linked List與一般陣列array 最大的不同在於Linked List使用的記憶體空間是分散的;而array、list則是使用連續的記憶體空間儲存
- Linked List加入或是刪除元素只需要改變pointer,但array若要新增刪除需要大量的資料搬移
- Linked List無法直接取得特定順序的值
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode()
        prev = prehead
        while list1 and list2:
            if list1.val <=list2.val:
                prev.next=list1  # prev決定好下一站要去list1
                list1=list1.next # 指標前進
            else:
                prev.next=list2  # prev決定好下一站要去list2
                list2=list2.next # 指標前進
            prev = prev.next     # prev指標(實際)前進到剛剛決定好的目標
        prev.next = list1 or list2 # prev的最後一站為非空的值
        return prehead.next