from typing import List

class Solution:
    def enumeration(self, l: List) -> int:
        length = len(l)
        result = 0
        current = 0
        for i in range(0, length):
            current = current + l[i] 
            if result < current or i == 0:
                result = current
            if current < 0:
                current = 0
        return result

    

s = Solution()
s.enumeration([31,-41,59,26,-53,58,97,-93,-23,84])