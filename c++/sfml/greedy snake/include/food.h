#ifndef SFML1_FOOD_H
#define SFML1_FOOD_H

#include <SFML/Graphics.hpp>
using namespace sf;

class Food{
private:
    int cell = 30;
    Texture foodTexture;
    RenderWindow* window;
public:
    Food(RenderWindow* window);
    Vector2f position;
    void render();
    void getPosition();
    void draw();
    void update(bool foodCollision);
};

#endif //SFML1_FOOD_H
