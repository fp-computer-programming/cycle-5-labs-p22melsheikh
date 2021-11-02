# MEE 11/1

import math
import time

t1_start = time.perf_counter()
math_pow = math.pow(2, 2)
t1_end = time.perf_counter()

t2_start = time.perf_counter()
math_reg = 2 ** 2
t2_end = time.perf_counter()

speed1 = t1_end - t1_start
speed2 = t2_end - t2_start

print(speed1)
print(speed2)
print(speed1 - speed2)