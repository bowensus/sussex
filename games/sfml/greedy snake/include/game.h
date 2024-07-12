#ifndef SFML1_GAME_H
#define SFML1_GAME_H

# include <SFML/Graphics.hpp>
#include "snake.h"
#include "food.h"
using namespace sf;

class Game{
private:
    int cell = 30;
    int m = 32, n = 24;
    int width = m * cell;
    int height = n * cell;
    RenderWindow window;
    Texture cellTexture;
    int fps = 60;
    Clock gameClock;
    bool foodCollision;
    bool bodyCollision;
    bool isGameOver;
    Snake snake;
    Food food;
public:
    Game();
    void input();
    void render();
    void draw();
    bool checkFoodCollision();
    bool checkBodyCollision();
    void loop();
    void run();
    ~Game();
};

#endif //SFML1_GAME_H
