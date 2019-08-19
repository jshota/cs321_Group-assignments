from typing import List
import numpy as np
import matplotlib.pyplot as plt
import sys
import time

class Count_Inversions:
    def __init__(self):
        self.count = 0
        self.list = []

    def brute_force(self) -> int:
        list = self.list
        size = len(self.list)
        self.count = 0
        for i in range(size-1):
            for j in range(i+1, size):
                if list[i] > list[j]:
                    self.count += 1
        return self.count

    def __helper_divide_and_conquer(self, list):
        size = len(list)
        mid = size // 2
        left_list  = list[:mid]
        right_list = list[mid:]
        if size > 1:
            self.__helper_divide_and_conquer(left_list)
            self.__helper_divide_and_conquer(right_list)
            # Merge-sorted sub arrays
            i, j = 0, 0
            for n in range(len(left_list) + len(right_list) + 1):
                if left_list[i] <= right_list[j]:
                    list[n] = left_list[i]
                    i += 1
                    if i == len(left_list) and j != len(right_list):
                        while j != len(right_list):
                            n += 1
                            list[n] = right_list[j]
                            j += 1
                        break
                elif left_list[i] > right_list[j]:
                    list[n] = right_list[j]
                    self.count += (len(left_list) - i)
                    j += 1
                    if j == len(right_list) and i != len(left_list):
                        while i != len(left_list):
                            n += 1
                            list[n] = left_list[i]
                            i += 1
                        break

    def divide_and_conquer(self) -> int:
        self.count = 0
        self.__helper_divide_and_conquer(self.list)
        return self.count

    def test(self):
        n_runs = 10
        bf_times = []
        dc_times = []
        vals1 = [x for x in range(100, 1000, 100)]
        vals2 = [x for x in range(1000, 10000, 1000)]
        vals = vals1 + vals2
        for val in vals:
            bf_time = 0
            dc_time = 0
            self.list = np.random.randint(1, 9, size=val)
            for i in range(n_runs):
                starttime = time.time()
                self.brute_force()
                endtime = time.time()
                bf_time += endtime - starttime

                starttime = time.time()
                self.divide_and_conquer()
                endtime = time.time()
                dc_time += endtime - starttime
            bf_times.append(bf_time / n_runs)
            dc_times.append(dc_time / n_runs)
        fig = plt.figure()
        plt.plot(vals, bf_times, label='brute-force')
        plt.plot(vals, dc_times, label='divide-and-conquer')
        plt.grid()
        plt.legend(loc='best')
        fig.savefig('result.png', dpi=fig.dpi)

c = Count_Inversions()
c.test()
