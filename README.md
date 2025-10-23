Benchmark quick Start:

python3 code/tools/benchmark.py
-> writes: output/results.csv

python3 code/tools/plot_results.py output/results.csv
-> writes: output/phase1_runtime.png

python3 code/tools/plot_memory.py output/results.csv
-> writes: output/phase1_memory.png

pip install numpy matplotlib psutil
-> if needed
