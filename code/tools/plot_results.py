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
        status = row["status"].strip().lower()

        if status == "ok":
            val = row["stdout_time_s"] if row["stdout_time_s"] else row["wall_time_s"]
            val = val.replace(",", ".")  # handle commas from locales
            t = float(val)
            data[lang].append((n, t))
        else:
            timeouts[lang].append(n)

plt.figure(figsize=(8, 5))
for lang, points in data.items():
    points.sort()
    xs = [n for n, _ in points]
    ys = [t for _, t in points]
    plt.plot(xs, ys, marker="o", label=lang)

    if lang in timeouts:
        y_last = ys[-1] if ys else 0
        plt.scatter(timeouts[lang][0], y_last, color="red", marker="x", s=80, label=f"{lang} timeout")

plt.xlabel("Matrix size n")
plt.ylabel("Execution time (s)")
plt.title("Matrix Multiplication – Runtime Comparison")
plt.xscale("log")
plt.yscale("log")
plt.grid(True, which="both", linestyle="--", linewidth=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("output/phase1_runtime.png", dpi=180)
plt.show()
