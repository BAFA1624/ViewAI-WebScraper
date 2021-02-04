cmake_minimum_required(VERSION 3.1)
project(TextParser)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_subdirectory(Parser)

add_executable(parser_test Parser/test.cpp)

target_link_libraries(parser_test PUBLIC Parser)

target_include_directories(Parser PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           "${PROJECT_SOURCE_DIR}/TextParser"
                           )

