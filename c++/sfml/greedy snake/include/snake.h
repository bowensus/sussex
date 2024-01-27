#ifndef SFML1_SNAKE_H
#define SFML1_SNAKE_H

#include <SFML/Graphics.hpp>
#include <vector>
using namespace sf;

class Snake{
private:
    int cell = 30;
    float interval = 0.1;
    float accumulatedTime = 0.0;
    Vector2f body;
    Vector2f tail;
    Texture snakeTexture;
    RenderWindow* window;
    Clock* gameClock;
public:
    Vector2f direction = {-1.0, 0.0};
    Vector2f head;
    std::vector<Vector2f> snakeBody = {};
    Snake(RenderWindow* window, Clock* gameClock);
    void getPosition();
    void render();
    void draw();
    void update(bool foodCollision);
    void handBorder();
};

#endif //SFML1_SNAKE_H
