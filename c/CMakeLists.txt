cmake_minimum_required(VERSION 3.16)
project(matrix_c C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_BUILD_TYPE Release)

add_executable(matrix_c matrix.c)

# Optional: enable optimizations
add_compile_options(-O3 -march=native)
