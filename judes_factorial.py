from math import factorial, log10, sqrt
from time import perf_counter
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def scatter(x, y, xlabel, ylabel,**kw):
    sns.scatterplot(x=x, y=y, **kw)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.xscale('log')
    # plt.yscale('log')
    plt.show()

def fac_time(N):  
    start_time = perf_counter()
    f = factorial(N)      
    elapsed_time = perf_counter() - start_time
    num_digits = len(str(f))
    # print('num', N, 'time', elapsed_time)
    return elapsed_time, num_digits


nums = list()
times = list()
digits = list()
for i in range(30, 80):
    num = int(1.15**i)
    t, d = fac_time(num)
    nums.append(num)
    times.append(t)
    digits.append(d)

print(times)
print(nums)

# scatter(nums, times)

scatter(nums, digits, 'N', '\'NUM\' DIGITS')
