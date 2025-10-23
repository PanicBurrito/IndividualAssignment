import random, argparse, time
parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, default=256)
args = parser.parse_args()
n = args.n

A = [[random.random() for _ in range(n)] for _ in range(n)]
B = [[random.random() for _ in range(n)] for _ in range(n)]
C = [[0.0 for _ in range(n)] for _ in range(n)]

t0 = time.time()
for i in range(n):
    Ai = A[i]
    Ci = C[i]
    for k in range(n):
        aik = Ai[k]
        Bk = B[k]
        for j in range(n):
            Ci[j] += aik * Bk[j]
t1 = time.time()
print(f"{t1 - t0:.6f}")
