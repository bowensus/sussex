#include "game.h"
#include <iostream>

Game::Game() : window(VideoMode(width, height), "tetris"), block(&window, &gameClock)
{
    window.setFramerateLimit(fps);

    font.loadFromFile("../font/AGoblinAppears-o2aV.ttf");
    render();
}

void Game::render()
{
    backTexture.loadFromFile("../graphics/background.png");

    frameTexture.loadFromFile("../graphics/frame.png");

    uiNextTexture.loadFromFile("../graphics/ui_next.png");

    lineText.setFont(font);
    lineText.setCharacterSize(24);
    lineText.setFillColor(Color::Black);
    lineText.setStyle(Text::Bold);

    scoreText.setFont(font);
    scoreText.setCharacterSize(24);
    scoreText.setFillColor(Color::Black);
    scoreText.setStyle(Text::Bold);

    overText.setFont(font);
    overText.setCharacterSize(48);
    overText.setFillColor(Color::White);
    overText.setStyle(Text::Bold);
}

void Game::input()
{
    Event sfmlEvent;
    while(window.pollEvent(sfmlEvent)){
        if(sfmlEvent.type == Event::Closed){
            window.close();
        }else if(sfmlEvent.type == Event::KeyPressed){
            switch(sfmlEvent.key.code){
                case Keyboard::Left:
                    if(block.checkMove("left")){
                        block.move("left", block.blockCurrent);
                    }
                    break;
                case Keyboard::Right:
                    if(block.checkMove("right")){
                        block.move("right", block.blockCurrent);
                    }
                    break;
                case Keyboard::Up:
                    if(block.shapeCurrent != 'O' && block.checkRotate()){
                        block.rotate(block.blockCurrent);
                    }
                    break;
                case Keyboard::Space:
                    block.accelerate = true;
                default:
                    break;
            }
        }
    }
}

void Game::draw()
{
    window.clear();

    Sprite backSprite(backTexture);
    window.draw(backSprite);

    Sprite frameSprite(frameTexture);
    frameSprite.setPosition(52, 80);
    window.draw(frameSprite);

    Sprite uiNextSprite(uiNextTexture);
    uiNextSprite.setPosition(422, 112);
    window.draw(uiNextSprite);

    lineText.setPosition(422, 380);
    scoreText.setPosition(422, 580);

    lineText.setString("Lines: \n\n" + std::to_string(line));
    window.draw(lineText);

    scoreText.setString("Score: \n\n" + std::to_string(score));
    window.draw(scoreText);
}

void Game::loop()
{
    while(window.isOpen()){

        if(checkOver()){
            showOver();
            window.display();
            sleep(seconds(5)); // 5s to see the screen
            break;
        }

        window.clear();
        input();
        draw();

        block.draw();
        block.update();

        calculateScore();
        changeSpeed();

        window.display();
    }
}

void Game::calculateScore()
{
    int ret = block.eliminateBlock();
    if(ret == 1){
        score += 1000;
    }else if(ret == 2){
        score += 3000;
    }else if(ret == 3){
        score += 6000;
    }else if(ret == 4){
        score += 10000;
    }
    line += ret;
}

void Game::changeSpeed()
{
    if(score >= 100000 && score < 200000){
        block.interval = 0.3;
    }else if(score >= 200000 && score < 300000){
        block.interval = 0.2;
    }else if(score >= 300000){
        block.interval = 0.1;
    }
}

bool Game::checkOver()
{
    for(const auto &item : block.playField){
        if(item.y < 2){
            return true;
        }
    }
    return false;
}

void Game::showOver()
{
    overText.setPosition(96, 224);

    overText.setString("Game Over");
    window.draw(overText);
}

void Game::run()
{
    loop();
}

Game::~Game()
{

}