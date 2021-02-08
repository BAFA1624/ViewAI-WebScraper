cmake_minimum_required(VERSION 3.1)
project(cparser)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED True)

add_compile_options(-Wall -Wextra -pedantic -O3)

add_library(simple_format_text simple_format_text.h simple_format_text.c)

add_executable(cparser_test test.c)

target_link_libraries(cparser_test PUBLIC simple_format_text)
