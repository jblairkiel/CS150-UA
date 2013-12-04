import os

def main():

    os.system('clear')
    board = createMatrix(20,30)
    snake = createSnake(board)
    head = snake[0]
    player = createPlayer(board)
    score = 0
    displayMatrix(board)
    for i in range(0, len(snake), 1):
        for j in range(0, len(snake[i]), 1):
            while(snake[i] != player):
                print("Score: ",score)
                choice = input("Enter j to move left, k to move right, i to move up and m to move down: ")
                if (choice == 'j'):
                    os.system('clear')
                    player = playerLeft(player,board)
                    snake = moveSnake(filteredHead(itemsHead(surroundHead(snake,player,board)),player),snake,score,board)
                    displayMatrix(board)
                    score = score +1
                elif (choice == 'k'):
                    os.system('clear')
                    player = playerRight(player,board)
                    snake = moveSnake(filteredHead(itemsHead(surroundHead(snake,player,board)),player),snake,score,board)
                    displayMatrix(board)
                    score = score +1
                elif (choice == 'i'):
                    os.system('clear')
                    player = playerUp(player, board)
                    snake = moveSnake(filteredHead(itemsHead(surroundHead(snake,player,board)),player),snake,score,board)
                    displayMatrix(board)
                    score = score +1
                elif (choice == 'm'):
                    os.system('clear')
                    player = playerDown(player,board)
                    snake = moveSnake(filteredHead(itemsHead(surroundHead(snake,player,board)),player),snake,score,board)
                    displayMatrix(board)
                    score = score +1
                else:
                    print("Penalty: Enter a valid move")
            if(snake[i] == player):
                os.system('clear')
                print("You lose for touching the snake")

def createArray(size):

    return ['-'] * size

def createMatrix(rows,cols):
    
    m = createArray(rows)
    for i in range(rows):
        m[i] = createArray(cols)
    return m

def displayMatrix(m):
    
    rows = len(m)
    cols = len(m[0])

    for r in range(0,rows,1):
        for c in range(0, cols, 1):
            print(m[r][c], end = ' ')
        print()
    return

def createSnake(matrix):

    snake = 'X'
    matrix[19][27] = snake
    matrix[19][28] = snake
    matrix[19][29] = snake
    return [[19,27],[19,28],[19,29]]

def surroundHead(snake, player, matrix):
    
    #filter touching itself
    surrounding = [[snake[0][0]-1,snake[0][1]],[snake[0][0]+1,snake[0][1]],[snake[0][0],snake[0][1]-1],[snake[0][0],snake[0][1]+1],[snake[0][0]+1,snake[0][1]+1],[snake[0][0]+1,snake[0][1]-1],[snake[0][0]-1,snake[0][1]+1],[snake[0][0]-1,snake[0][1]-1]]
    items = []
    for i in range(0, len(surrounding),1):
        if (surrounding[i] != snake[1]):
            items.append(surrounding[i])
    return items

def itemsHead(items):

    #filter in range
    filtered = []
    for i in range(0, len(items),1):
        if ((21 > items[i][0] > -1) and (31 > items[i][1] > -1)):
            filtered.append(items[i])
    return filtered

def filteredHead(filtered,player):

    #filter closest
    ishortest = 50
    for i in range(0, len(filtered),1):
        if (distance(filtered[i], player) < ishortest):
            ishortest = distance(filtered[i],player)
            final = [filtered[i][0], filtered[i][1]]
    return final


def moveSnake(newhead,snake,score,matrix):
    
    if(score % 5 == 0 and score != 0):
        snake.insert(0,newhead)
        matrix[snake[0][0]][snake[0][1]] = 'X'
    else:
        matrix[snake[len(snake)-1][0]][snake[len(snake)-1][1]] = '-'
        snake.insert(0,newhead)
        snake.pop()
        matrix[snake[0][0]][snake[0][1]] = 'X'
    return snake

def createPlayer(matrix):
    
    player = 'i'
    matrix[0][0] = player
    return [0,0]

def playerLeft(player,matrix):
    
    if(player[1]-1 >= 0):
        matrix[player[0]][player[1]] = '-'
        player[1] = player [1]-1
        matrix[player[0]][player[1]] = 'i'
    return player

def playerRight(player,matrix):
    
    if(player[1]-1 < 30):
        matrix[player[0]][player[1]] = '-'
        player[1] = player[1]+1
        matrix[player[0]][player[1]] = 'i'
    else:
        print("Stay inside of the board!")
        player[1] = player[1]
    return player
        

def playerUp(player,matrix):
    
    if(player[0]-1 >= 0):
        matrix[player[0]][player[1]] = '-'
        player[0] = player[0]-1
        matrix[player[0]][player[1]] = 'i'
    return player 

def playerDown(player,matrix):

    if(player[0]+1 < 20):
        matrix[player[0]][player[1]] = '-'
        player[0] = player[0]+1
        matrix[player[0]][player[1]] = 'i'
    else:
        print("Stay inside of the board!")
        player[1] = player[1]
    return player

def distance(one,two):

    z = one[0] - two[0]
    y = one[1] - two[1]
    distance = abs(z)+abs(y)
    return abs(distance)

main()
