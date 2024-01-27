cmake_minimum_required(VERSION 3.26)
project(sfml1)

set(CMAKE_CXX_STANDARD 17)

# static link
# copy dll file by yourself

set(SFML_INCLUDE_DIR D:/SFML/include)
set(SFML_LIB_DIR D:/SFML/lib)

include_directories(${SFML_INCLUDE_DIR})

link_directories(${SFML_LIB_DIR})

add_executable(sfml1 game/main.cpp
        game/game.cpp
        game/game.h
        game/snake.cpp
        game/snake.h
        game/food.cpp
        game/food.h)

target_link_libraries(sfml1 PRIVATE sfml-graphics sfml-window sfml-system)
