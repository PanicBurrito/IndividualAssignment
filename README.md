# Matrix Benchmarking

Monorepo mit drei Implementierungen (`C`, `Java`, `Python`) für Matrix-Funktionen/Benchmarks.

## Struktur
```
matrix-bench/
├─ c/
│  ├─ matrix.c
│  └─ CMakeLists.txt
├─ java/
│  └─ src/
│     └─ Matrix.java
└─ python/
   └─ matrix.py
```

## Quickstart

### C (CLion oder Terminal)
```bash
cd c
# Terminal Build
cc -O3 -march=native -std=c11 matrix.c -o matrix_c
./matrix_c
```

Oder mit CMake (z. B. in CLion automatisch):
```bash
cd c
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
./build/matrix_c
```

### Java (IntelliJ IDEA)
- Öffne `java/` als Projekt (ohne Maven).
- Stelle sicher, dass ein JDK (17 oder 21) gesetzt ist.
- Run: Rechtsklick auf `Matrix.java` → **Run 'Matrix.main()'**.

Terminal-Alternative:
```bash
cd java/src
javac Matrix.java
java Matrix
```

### Python (IntelliJ mit Python-Plugin oder Terminal)
```bash
cd python
python3 -m venv .venv
source .venv/bin/activate
python matrix.py
```

## Git & GitHub

Neues Repo lokal initialisieren:
```bash
cd matrix-bench
git init
git add .
git commit -m "Initial commit: C/Java/Python matrix baseline"
git branch -M main
```

### Remote hinzufügen (wähle **eine** Variante)

**SSH (empfohlen):**
```bash
git remote add origin git@github.com:<DEIN-USER>/matrix-bench.git
git push -u origin main
```

**HTTPS:**
```bash
git remote add origin https://github.com/<DEIN-USER>/matrix-bench.git
git push -u origin main
```

## IDE-Hinweise
- **IntelliJ (Java):** Kein Maven nötig. Wenn du Packages nutzt, achte auf passenden Ordnerpfad.
- **CLion (C):** Toolchain (Xcode CLTs) muss installiert sein (`xcode-select --install`).
- **Python:** Interpreter/Virtualenv im Projekt setzen.

---

> Tipp: Für reproduzierbare Benchmarks später gerne `README` ergänzen (Argumente, Daten, Timing).
