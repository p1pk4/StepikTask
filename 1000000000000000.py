# Python, не умирай плз
import time

t = time.process_time()

x = sum(range(10000000000))

print(x)

print(time.process_time() - t, 'seconds')