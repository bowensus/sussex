#include "food.h"

Food::Food(RenderWindow* window) : window(window)
{
    getPosition();
}

void Food::render()
{
    foodTexture.loadFromFile("../graphics/red.png");
}

void Food::getPosition()
{
    position.x = static_cast<float>(rand() % static_cast<int>(window->getSize().x));
    position.y = static_cast<float>(rand() % static_cast<int>(window->getSize().y));

    position.x = static_cast<int>(position.x / cell);
    position.y = static_cast<int>(position.y / cell);
}

void Food::draw()
{
    Sprite foodSprite(foodTexture);
    foodSprite.setScale(static_cast<float>(cell) / foodTexture.getSize().x, static_cast<float>(cell) / foodTexture.getSize().y);

    foodSprite.setPosition(position.x * cell, position.y * cell);
    window->draw(foodSprite);
}

void Food::update(bool foodCollision)
{
    if(foodCollision){
        getPosition();
    }
}
