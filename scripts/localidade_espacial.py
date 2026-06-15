import time
import numpy as np

N = 10_000_000
arr = np.arange(N)

inicio = time.perf_counter()
for i in range(N):
    x = arr[i]
fim = time.perf_counter()
print("Sequencial:", fim - inicio)

inicio = time.perf_counter()
for i in range(0, N, 16):
    x = arr[i]
fim = time.perf_counter()
print("Saltos:", fim - inicio)
