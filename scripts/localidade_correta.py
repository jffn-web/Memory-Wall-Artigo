import numpy as np
import time

N = 50_000_000
arr = np.arange(N, dtype=np.int32)

inicio = time.perf_counter()
soma = 0
for i in range(N):
    soma += int(arr[i])
fim = time.perf_counter()
print("Sequencial", fim - inicio)

inicio = time.perf_counter()
soma = 0
for offset in range(16):
    for i in range(offset, N, 16):
        soma += int(arr[i])
fim = time.perf_counter()
print("Saltos", fim - inicio)
