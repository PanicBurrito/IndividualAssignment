import subprocess, sys, csv, time, os, signal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
C_DIR = ROOT / "code" / "c"
JAVA_DIR = ROOT / "code" / "java" / "src"
PY_DIR = ROOT / "code" / "python"

SIZES = [10, 100, 1000, 10000]
TIMEOUT = 300

def run_with_rss(cmd, timeout_sec):
    time_bin = "/usr/bin/time"
    use_time = os.path.exists(time_bin)
    full = f'{time_bin} -l {cmd}' if use_time else cmd
    t0 = time.time()
    try:
        proc = subprocess.run(full, shell=True, capture_output=True, text=True, timeout=timeout_sec)
        t1 = time.time()
        stdout, stderr = proc.stdout.strip(), proc.stderr.strip()
        rss = None
        if use_time:
            for line in stderr.splitlines():
                if "maximum resident set size" in line.lower():
                    try:
                        rss = int(line.strip().split()[0])
                    except Exception:
                        pass
        return "ok", t1 - t0, rss, stdout, stderr
    except subprocess.TimeoutExpired:
        return "timeout", None, None, "", ""

def build_c():
    exe = C_DIR / "matrix_arg"
    src = C_DIR / "matrix_arg.c"
    cmd = f'cc -O3 -march=native -std=c11 "{src}" -o "{exe}"'
    subprocess.run(cmd, shell=True, check=True)
    return exe

def build_java():
    src = JAVA_DIR / "MatrixArg.java"
    cmd = f'javac "{src}"'
    subprocess.run(cmd, shell=True, check=True)
    return JAVA_DIR / "MatrixArg"

def ensure_numpy():
    try:
        import numpy
    except ImportError:
        print("Installing numpy...", file=sys.stderr)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])

def main():
    exe_c = build_c()
    build_java()
    ensure_numpy()

    results_path = ROOT / "output" / "results.csv"
    results_path.parent.mkdir(parents=True, exist_ok=True)

    with open(results_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["language", "n", "status", "wall_time_s", "max_rss", "stdout_time_s"])

        for n in SIZES:
            print(f"\n===== Matrix size n={n} =====")

            status, wt, rss, out, err = run_with_rss(f'"{exe_c}" {n}', TIMEOUT)
            w.writerow(["c", n, status, f"{wt:.6f}" if wt else "", rss if rss else "", out.strip()])
            print(f"C: {status}, {wt}")

            status, wt, rss, out, err = run_with_rss(f'java -Xmx4G -cp "{JAVA_DIR}" MatrixArg {n}', TIMEOUT)
            w.writerow(["java", n, status, f"{wt:.6f}" if wt else "", rss if rss else "", out.strip()])
            print(f"Java: {status}, {wt}")

            status, wt, rss, out, err = run_with_rss(f'python3 "{PY_DIR / "matrix_pure.py"}" --n {n}', TIMEOUT)
            w.writerow(["python_pure", n, status, f"{wt:.6f}" if wt else "", rss if rss else "", out.strip()])
            print(f"Python pure: {status}, {wt}")

            status, wt, rss, out, err = run_with_rss(f'python3 "{PY_DIR / "matrix_numpy.py"}" --n {n}', TIMEOUT)
            w.writerow(["python_numpy", n, status, f"{wt:.6f}" if wt else "", rss if rss else "", out.strip()])
            print(f"Python NumPy: {status}, {wt}")

    print("\n Benchmark completed. Results saved to:", results_path)

if __name__ == "__main__":
    main()