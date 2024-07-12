#include "snake.h"

Snake::Snake(RenderWindow* window, Clock* gameClock)
    : window(window),
      gameClock(gameClock)
{
    getPosition();
    snakeBody.push_back(head);
    body = head - direction;
    for(int i=0; i<2; i++){
        snakeBody.push_back(body);
        body -= direction;
    }
}

void Snake::render()
{
    snakeTexture.loadFromFile("../graphics/green.png");
}

void Snake::getPosition()
{
    head.x = static_cast<float>(rand() % static_cast<int>(window->getSize().x));
    head.y = static_cast<float>(rand() % static_cast<int>(window->getSize().y));

    // set pos into cell(int)
    head.x = static_cast<int>(head.x / cell);
    head.y = static_cast<int>(head.y / cell);
}

void Snake::draw()
{
    Sprite snakeSprite(snakeTexture);
    snakeSprite.setScale(static_cast<float>(cell) / snakeTexture.getSize().x, static_cast<float>(cell) / snakeTexture.getSize().y);

    for(const auto& pos : snakeBody){
        snakeSprite.setPosition(pos.x * cell, pos.y * cell);
        window->draw(snakeSprite);
    }
}

void Snake::update(bool foodCollision)
{
    float elapsedTime = gameClock->restart().asSeconds(); // elapsedTime = 1/fps
    accumulatedTime += elapsedTime;

    if(accumulatedTime >= interval){
        accumulatedTime -= interval;

        head += direction;
        snakeBody.insert(snakeBody.begin(), head);

        tail = snakeBody.back();
        snakeBody.pop_back();
    }

    if(foodCollision){
        snakeBody.push_back(tail);
    }

    handBorder();
}

void Snake::handBorder()
{
    int widthCell = window->getSize().x / cell;
    int heightCell = window->getSize().y / cell;

    // border = -1 not 0 ???
    if(head.x < -1){
        head.x = static_cast<float>(widthCell);
    }else if(head.x > widthCell){
        head.x = -1;
    }

    if(head.y < -1){
        head.y = static_cast<float>(heightCell);
    }else if(head.y > heightCell){
        head.y = -1;
    }
}

