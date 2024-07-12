#ifndef SFML2_BLOCK_H
#define SFML2_BLOCK_H
#include <SFML/Graphics.hpp>
using namespace sf;

class Block{
private:
    int cell = 32;
    Texture blockTexture;
    RenderWindow* window;
    Clock* gameClock;
    float accumulatedTime = 0.0;
public:
    float interval = 0.4;
    bool accelerate = false;

    char shapeCurrent;
    char shapeNext;
    std::vector<Vector2f> blockCurrent;
    std::vector<Vector2f> blockNext;
    std::vector<Vector2f> playField;

    Block(RenderWindow* window, Clock* gameClock);
    std::vector<Vector2f> generateBlock(char &shape);

    void render();
    void draw();
    void fall();
    void move(std::string order, std::vector<Vector2f> &blockBody);
    void rotate(std::vector<Vector2f> &blockBody);

    bool checkMove(std::string order);
    bool checkRotate();
    bool checkBottom();

    void refreshNewBlock();
    int eliminateBlock();

    void update();
};


#endif //SFML2_BLOCK_H
