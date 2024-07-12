cmake_minimum_required(VERSION 3.27)
project(sfml2)

set(CMAKE_CXX_STANDARD 17)

set(SFML_INCLUDE_DIR D:/SFML/include)
set(SFML_LIB_DIR D:/SFML/lib)

include_directories(${SFML_INCLUDE_DIR})
link_directories(${SFML_LIB_DIR})

add_executable(sfml2 main.cpp
        game.h
        block.cpp
        game.cpp)

target_link_libraries(sfml2 PRIVATE sfml-graphics sfml-window sfml-system)
