import csv, sys
import matplotlib.pyplot as plt
from collections import defaultdict

path = sys.argv[1] if len(sys.argv) > 1 else "output/results.csv"

data = defaultdict(list)
timeouts = defaultdict(list)

with open(path, newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        lang = row["language"]
        n = int(row["n"])
        status = (row["status"] or "").strip().lower()
        if status != "ok":
            timeouts[lang].append(n)
            continue

        raw = (row["max_rss"] or "").strip()
        if not raw:
            continue
        try:
            rss = int(raw)
            mb = rss / (1024 * 1024) if rss > 10_000_000 else rss / 1024
            data[lang].append((n, mb))
        except ValueError:
            continue

plt.figure(figsize=(8, 5))
for lang, pts in data.items():
    pts.sort()
    xs = [n for n, _ in pts]
    ys = [mb for _, mb in pts]
    plt.plot(xs, ys, marker="o", label=lang)

    if timeouts.get(lang):
        y_last = ys[-1] if ys else 0
        plt.scatter(timeouts[lang][0], y_last, marker="x", s=80, color="red", label=f"{lang} timeout")

plt.xlabel("Matrix size n")
plt.ylabel("Maximum memory usage (MB)")
plt.title("Matrix Multiplication – Memory Consumption")
plt.xscale("log")
plt.yscale("log")
plt.grid(True, which="both", linestyle="--", linewidth=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("output/phase1_memory.png", dpi=180)
plt.show()