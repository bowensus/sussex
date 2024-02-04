#include "block.h"
#include <iostream>
#include <cstdlib>
#include <ctime>

Block::Block(RenderWindow* window, Clock* gameClock) : window(window), gameClock(gameClock)
{
    render();
    blockCurrent = generateBlock(shapeCurrent);
    blockNext = generateBlock(shapeNext);
}

std::vector<Vector2f> Block::generateBlock(char &shape)
{
    Vector2f ctr = {7, 2};

    std::vector<Vector2f> blockCase;

    std::srand(static_cast<unsigned int>(std::time(nullptr)));
    int num = std::rand() % 7;

    switch(num){
        case 0: shape = 'I'; break;
        case 1: shape = 'O'; break;
        case 2: shape = 'T'; break;
        case 3: shape = 'S'; break;
        case 4: shape = 'Z'; break;
        case 5: shape = 'J'; break;
        case 6: shape = 'L'; break;
    }

    if(shape == 'I'){
        blockCase = {{ctr.x-1, ctr.y}, {ctr.x, ctr.y}, {ctr.x+1, ctr.y}, {ctr.x-2, ctr.y}};
    }else if(shape == 'O'){
        blockCase = {{ctr.x-1, ctr.y}, {ctr.x, ctr.y}, {ctr.x-1, ctr.y-1}, {ctr.x, ctr.y-1}};
    }else if(shape == 'T'){
        blockCase = {{ctr.x-1, ctr.y-1}, {ctr.x, ctr.y}, {ctr.x, ctr.y-1}, {ctr.x+1, ctr.y-1}};
    }else if(shape == 'S'){
        blockCase = {{ctr.x-1, ctr.y}, {ctr.x, ctr.y}, {ctr.x, ctr.y-1}, {ctr.x+1, ctr.y-1}};
    }else if(shape == 'Z'){
        blockCase = {{ctr.x+1, ctr.y}, {ctr.x, ctr.y}, {ctr.x, ctr.y-1}, {ctr.x-1, ctr.y-1}};
    }else if(shape == 'J'){
        blockCase = {{ctr.x-1, ctr.y}, {ctr.x, ctr.y}, {ctr.x-1, ctr.y-1}, {ctr.x+1, ctr.y}};
    }else if(shape == 'L'){
        blockCase = {{ctr.x-1, ctr.y}, {ctr.x, ctr.y}, {ctr.x+1, ctr.y}, {ctr.x+1, ctr.y-1}};
    }
    return blockCase;
}

void Block::render()
{
    if(interval <= 0.1){
        blockTexture.loadFromFile("../graphics/green_block.png");
    }else if(interval <= 0.2 && interval > 0.1){
        blockTexture.loadFromFile("../graphics/yellow_block.png");
    }else if(interval <= 0.3 && interval > 0.2){
        blockTexture.loadFromFile("../graphics/red_block.png");
    }else{
        blockTexture.loadFromFile("../graphics/blue_block.png");
    }

}

void Block::draw()
{
    Sprite blockSprite(blockTexture);

    for(const auto &item : blockCurrent){
        blockSprite.setPosition(cell * item.x, cell * item.y);
        if(item.y > 2){
            window->draw(blockSprite);
        }
    }

    for(const auto &item : playField){
        blockSprite.setPosition(cell * item.x, cell * item.y);
        window->draw(blockSprite);
    }

    for(const auto &item : blockNext){
        blockSprite.setPosition(cell * item.x + 288, cell * item.y + 160);
        window->draw(blockSprite);
    }
}

void Block::fall()
{
    for(Vector2f &item : blockCurrent){
        item.y += 1;
    }
}

void Block::move(std::string order, std::vector<Vector2f> &blockBody)
{
    if(order == "left"){
        for(Vector2f &item : blockBody){
            item.x -= 1;
        }
    }else if(order == "right"){
        for(Vector2f &item : blockBody){
            item.x += 1;
        }
    }
}

void Block::rotate(std::vector<Vector2f> &blockBody)
{
    Vector2f centre = blockBody[1];

    if(shapeCurrent == 'I'){
        for(Vector2f &item : blockBody){
            int x = centre.x - item.x;
            int y = centre.y - item.y;
            if(item.y == centre.y){
                item.x += x;
                item.y -= x;
            }else if(item.x == centre.x){
                item.x -= y;
                item.y += y;
            }
        }
        return;
    }

    for(Vector2f &item : blockBody){
        if(item.y == centre.y){
            if(item.x < centre.x){
                item.x += 1;
                item.y -= 1;
            }else if(item.x > centre.x){
                item.x -= 1;
                item.y += 1;
            }
        }else if(item.x == centre.x){
            if(item.y < centre.y){
                item.x += 1;
                item.y += 1;
            }else if(item.y > centre.y){
                item.x -= 1;
                item.y -= 1;
            }
        }else if(item.x < centre.x && item.y < centre.y){
            item.x += 2;
        }else if(item.x > centre.x && item.y < centre.y){
            item.y += 2;
        }else if(item.x > centre.x && item.y > centre.y){
            item.x -= 2;
        }else if(item.x < centre.x && item.y > centre.y){
            item.y -= 2;
        }
    }
}

// use a copy to check border firstly before moving
bool Block::checkMove(std::string order)
{
    std::vector<Vector2f> blockPossible = blockCurrent;
    move(order, blockPossible);

    for(const auto &item : blockPossible){
        if(item.x < 2 || item.x > 11){
            return false;
        }
        auto it = std::find(playField.begin(), playField.end(), item);
        if(it != playField.end()){
            return false;
        }
    }

    return true;
}

bool Block::checkRotate()
{
    std::vector<Vector2f> blockPossible = blockCurrent;
    rotate(blockPossible);
    for(const auto &item : blockPossible){
        if(item.x < 2 || item.x > 11){
            return false;
        }
        auto it = std::find(playField.begin(), playField.end(), item);
        if(it != playField.end()){
            return false;
        }
    }
    return true;
}

bool Block::checkBottom()
{
    for(const auto &item : blockCurrent){
        Vector2f itemFind = {item.x, item.y+1};
        auto it = std::find(playField.begin(), playField.end(), itemFind);
        if(it != playField.end() || item.y == 22){
            return true;
        }
    }
    return false;
}

void Block::refreshNewBlock()
{
    for(const auto &item : blockCurrent){
        playField.push_back(item);
    }
    blockCurrent = blockNext;
    shapeCurrent = shapeNext;
    blockNext = generateBlock(shapeNext);
    accelerate = false;
}

int Block::eliminateBlock()
{
    int cnt = 0;
    std::vector<int> rowFull = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
    std::vector<int> rowCheck;
    for(int i=3; i<=23; i++){
        // i = row
        rowCheck.clear();
        for(const auto &item : playField){
            if(item.y == i){
                rowCheck.push_back(item.x);
            }
        }
        std::sort(rowCheck.begin(), rowCheck.end());

        if(rowFull == rowCheck){
            // eliminate this row if true
            int yToRemove = i;
            playField.erase(std::remove_if(playField.begin(), playField.end(),
                                           [yToRemove](const Vector2f& item) {return item.y == yToRemove;}), playField.end());
            cnt += 1;

            for(auto &item : playField){
                if(item.y < i){
                    item.y += 1;
                }
            }
        }

    }

    return cnt;
}

void Block::update()
{
    float elapsedTime = gameClock->restart().asSeconds();
    accumulatedTime += elapsedTime;

    if(accumulatedTime >= interval && !accelerate){
        accumulatedTime -= interval;
        fall();
    }else if(accumulatedTime >= 0.05 && accelerate){
        accumulatedTime -= 0.05;
        fall();
    }

    if(checkBottom()){
        refreshNewBlock();
    }
}
