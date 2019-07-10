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
        length = len(l)
        for i in range(0, length):
            current = 0
            for j in range(i, length):
                current = current + l[j]
                if result < current or j == 0:
                    result = current
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

test_list = [-18, -47, -40, -43, -2, 48, 31, -24, 36, -49, 4, -29, -4, -39, 12, 24, 8, 40, 45, -17, 6, -11, -5, -30, -8, 25, -44, -9, -20, -50, -12, -32, 41, 10, -42, -15, 11, -38, 37, 21, 33, -22, 16, -41, -46, -33, -26, 7, -3, -28, 29, 20, 27, 3, 15, 49, 23, -1, 14, 32, -31, -13, -48, -14, 13, 39, 46, -35, -36, 0, 17, -27, -21, 28, -7, 44, -10, 34, -19, 47, 42, -34, 5, 26, -45, 35, 9, -25, 38, -37, -23, 22, -6, -16, 18, 43, 30, 2, 19, 1]
s = Solution()
print(s.enumeration(test_list))
print(s.better_enumeration(test_list))
print(s.dynamic(test_list))