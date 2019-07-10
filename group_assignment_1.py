from typing import List

class Solution:
    def enumeration(self, l: List) -> int:
        result = 0
        length = len(l)
        for i in range(0, length):
            for j in range(i, length):
                current = 0
                for n in range(j, length):
                    current += l[n]
                    if result < current or n == 0:
                        result = current
        return result

    def better_enumeration(self, l: List) -> int:
        result = 0
        current = 0
        for i in range(0, len(l)):
            current = current + l[i]
            print(current)
            if result < current or i == 0:
                result = current
            if current < 0:
                current = 0
        return result

    def dynamic(self, l:List) -> int:
        current = [[0] * (len(l)+1) for i in range(len(l)+1)]
        current[0] = 0
        for j in range(1, len(current)):
            current[j] = max(current[j-1]+l[j-1],l[j-1])
            result = current[0]
        for j in range(1, len(current)):
            if result < current[j]:
                result = current[j]
        return result

test_list = [31,-41,59,26,-53,58,97,-93,-23,84]
s = Solution()
s.enumeration(test_list)
s.better_enumeration(test_list)
s.dynamic(test_list)