#ifndef SFML2_GAME_H
#define SFML2_GAME_H
#include <SFML/Graphics.hpp>
#include "block.h"

using namespace sf;

class Game{
private:
    int cell = 32;
    int x = 20, y = 25;
    int width = x * cell;
    int height = y * cell;
    RenderWindow window;
    Texture backTexture;
    Texture frameTexture;
    Texture uiNextTexture;
    int fps = 60;
    Clock gameClock;
    Block block;
    int line = 0;
    int score = 0;
    Font font;
    Text scoreText;
    Text lineText;
    Text overText;
public:
    Game();
    void render();
    void input();
    void draw();
    void calculateScore();
    void changeSpeed();
    bool checkOver();
    void showOver();
    void loop();
    void run();
    ~Game();
};


#endif //SFML2_GAME_H
