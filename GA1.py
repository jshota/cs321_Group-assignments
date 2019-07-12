from typing import List
from time import perf_counter
from enum import Enum
import random

class test_function (Enum):
    enumeration = 1
    better_enumeration = 2
    dynamic = 3

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

    # def dynamic(self, l:List) -> int:
    #     current = [[0] * (len(l)+1) for i in range(len(l)+1)]
    #     current[0] = 0
    #     result = 0
    #     for j in range(1, len(current)):
    #         current[j] = max(current[j-1]+l[j-1],l[j-1])
    #     for j in range(1, len(current)):
    #         if result < current[j]:
    #             result = current[j]
    #     return result

    def dynamic(self, l:List) -> int:
        current = 0
        result = 0
        for i in range(0, len(l)):
            current += l[i]
            if current < 0:
                current = 0
            if result < current:
                result = current
        return result

    def test(self, test_function, size_list: List, file):
        print('Processing')
        
        for s in size_list:
            for i in range(1, 10):
                test_list = []
                for j in range(i*s):
                    test_list.append(random.randint(-100,100))
                start = perf_counter()
                if test_function == test_function.enumeration:
                    self.enumeration(test_list)
                elif test_function == test_function.better_enumeration:
                    self.better_enumeration(test_list)
                else:
                    self.dynamic(test_list)
                stop = perf_counter()
                file.write('Array size: ' + str(len(test_list)) + '\n')
                file.write('Run time: ' + str(stop - start) + ' s\n' + '****\n')
                print('.')

s = Solution()
fo = open("result.txt", "w")
fo.write('enumeration\n')
s.test(test_function.enumeration, [100], fo)
fo.write('better_enumeration\n')
s.test(test_function.better_enumeration, [100, 1000], fo)
fo.write('dynamic\n')
s.test(test_function.dynamic, [100, 1000], fo)
fo.close()
