import argparse, time
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, default=1024)
args = parser.parse_args()
n = args.n

A = np.random.rand(n, n)
B = np.random.rand(n, n)

t0 = time.time()
C = A @ B
t1 = time.time()
print(f"{t1 - t0:.6f}")
