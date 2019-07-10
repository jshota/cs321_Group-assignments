from typing import List

class Solution:
    def enumeration(self, l:list) -> int:
        result_list = []
        result = 0
        for i in range(0, len(l)):
            for j in range(i, len(l)):
                result += l[j]
            result_list.append(result)
        return max(result_list)

    def better_enumeration(self, l: List) -> int:
        result = None
        current = None
        for i in range(0, len(l)):
            current = current + l[i] 
            if result < current or i == 0:
                result = current
            if current < 0:
                current = 0
        return result

s = Solution()
s.enumeration([31,-41,59,26,-53,58,97,-93,-23,84])