#############
# Author : Yujun Wen
# Last edit: 2022/8/1
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 太難了先跳過

"""
class Solution:
    def read(self, buf: List[str], n: int) -> int:
        copied_chars = 0
        read_chars = 4
        buf4 = [''] * 4

        while copied_chars < n and read_chars == 4:
            read_chars = read4(buf4)

            for i in range(read_chars):
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i]
                copied_chars += 1

        return copied_chars
        
        
        