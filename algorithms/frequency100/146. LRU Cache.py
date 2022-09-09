#############
# Author : Yujun Wen
# Last edit: 2022/9/10
# email: yujunwen0517@gmail.com
#####
"""
Note
這題須要學到OrderedDict的屬性
move_to_end: 將現有的 key 移動到 ordered dictionary 的任一端。如果 last 為True值(此為預設值)則將元素移至右端;如果 last 為False值則將元素移至左端
popitem: 如果 last 為True值,則按 LIFO 後進先出的順序回傳鍵值對,否則就按 FIFO 先進先出的順序回傳鍵值對
(這題蠻常考的要掌握)
1.get的重點是set key as the newest one,保持資料
Time complexity: O(1) 
Space complexity O(capacity) 
"""
class LRUCache():

    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        
        self.dic.move_to_end(key) # 將key移動至最右邊
        return self.dic[key]
        

    def put(self, key, value):
        if key in self.dic:    
            self.dic.move_to_end(key)# 將key移動至最右邊
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:  # self.dic is full
                self.dic.popitem(last=False) #FIFO,因此最左邊的會先被踢出去
        self.dic[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# test case
# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]