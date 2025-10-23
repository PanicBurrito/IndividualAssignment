Benchmark quick Start:

python3 tools/benchmark.py
-> writes: tools/results.csv

python3 tools/plot_runtime.py tools/results.csv
-> writes: tools/phase1_runtime.png

python3 tools/plot_memory.py tools/results.csv
-> writes: tools/phase1_memory.png

pip install numpy matplotlib psutil
-> if needed
