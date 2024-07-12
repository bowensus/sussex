#include "game.h"
# include <SFML/Graphics.hpp>

Game::Game()
    : window(VideoMode(width, height), "greedy snake"),
      snake(&window, &gameClock),
      food(&window)
{
    window.setFramerateLimit(fps);
}

void Game::input()
{
    Event sfmlEvent;

    while(window.pollEvent(sfmlEvent)){
        if(sfmlEvent.type == Event::Closed){
            window.close();
        }
        else if(sfmlEvent.type == Event::KeyPressed){
            switch(sfmlEvent.key.code){
                case Keyboard::Up:
                    if(snake.direction.y == 0.0){
                        snake.direction = {0.0, -1.0};
                    }
                    break;
                case Keyboard::Down:
                    if(snake.direction.y == 0.0){
                        snake.direction = {0.0, 1.0};
                    }
                    break;
                case Keyboard::Left:
                    if(snake.direction.x == 0.0){
                        snake.direction = {-1.0, 0.0};
                    }
                    break;
                case Keyboard::Right:
                    if(snake.direction.x == 0.0){
                        snake.direction = {1.0, 0.0};
                    }
                    break;
                default:
                    break;
            }
        }
    }
}

void Game::render()
{
    cellTexture.loadFromFile("../graphics/white.png");

    snake.render();
    food.render();
}

void Game::draw()
{
    window.clear();

    Sprite cellSprite(cellTexture);
    cellSprite.setScale(static_cast<float>(cell) / cellTexture.getSize().x, static_cast<float>(cell) / cellTexture.getSize().y);

    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            cellSprite.setPosition(static_cast<float>(i * cell), static_cast<float>(j * cell));
            window.draw(cellSprite);
        }
    }
}

void Game::loop()
{
    while(window.isOpen()){

        isGameOver = checkBodyCollision();

        input();

        if (isGameOver) {
            window.close();
            break;
        }

        draw();
        foodCollision = checkFoodCollision();

        snake.update(foodCollision);
        snake.draw();

        food.update(foodCollision);
        food.draw();

        window.display();
    }
}

bool Game::checkFoodCollision()
{
    for(const auto& pos : snake.snakeBody){
        if(pos == food.position){
            return true;
        }
    }
    return false;
}

bool Game::checkBodyCollision()
{
    int num = snake.snakeBody.size();
    for(int i=1; i<num; i++){
        if(snake.head == snake.snakeBody[i]){
            return true;
        }
    }
    return false;
}

void Game::run()
{
    render();
    loop();
}

Game::~Game()
{

}
