from List import *
import os
import random

def main():

    os.system('clear')
    board = createMatrix(20,30)
    snake = createSnake(board)
    token = placeToken(board)
    head = snake[0]
    displayMatrix(board)
    for i in range(0, len(snake), 1):
        for j in range(0, len(snake[i]), 1):
            while(snakeDead(board,head,snake) == False):
                choice = input("Enter j to move left, k to move right, i to move up and m to move down: ")
                if (choice == 'j'):
                    os.system('clear')
                    snake = snakeLeft(snake,board,token)
                    displayMatrix(board)
                    
                elif (choice == 'k'):
                    os.system('clear')
                    snake = snakeRight(snake,board,token)
                    displayMatrix(board)

                elif (choice == 'i'):
                    os.system('clear')
                    snake = snakeUp(snake,board,token)
                    displayMatrix(board)

                elif (choice == 'm'):
                    os.system('clear')
                    snake = snakeDown(snake,board,token)
                    displayMatrix(board)

                else:
                    print("Penalty: Enter a valid move")

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

    snake = "x"
    head = '@'
    matrix[19][25] = head
    matrix[19][26] = snake
    matrix[19][27] = snake
    matrix[19][28] = snake
    matrix[19][29] = snake
    return [[19,25],[19,26],[19,27],[19,28],[19,29]]

def snakeLeft(snake,matrix,token):

    newhead = [snake[0][0],snake[0][1]-1]
    if (newhead == token):
        snake.insert(0,newhead)
        matrix[newhead[0]][newhead[1]] = '@'
        matrix[snake[1][0]][snake[1][1]] = 'x'
        matrix[snake[len(snake)-1][0]][snake[len(snake)-1][1]] ='-'
        token = restartToken(matrix)
    else:   
        snake.insert(0,newhead)
        matrix[newhead[0]][newhead[1]] = '@'
        matrix[snake[1][0]][snake[1][1]] = 'x'
        matrix[snake[len(snake)-1][0]][snake[len(snake)-1][1]] = '-'
        snake.pop()
    return snake

def snakeRight(snake,matrix,token):

    newhead = [snake[0][0],snake[0][1]+1]
    if (newhead == token):
        snake.insert(0,newhead)
        matrix[newhead[0]][newhead[1]] = '@'
        matrix[snake[1][0]][snake[1][1]] = 'x'
        matrix[snake[len(snake)-1][0]][snake[len(snake)-1][1]] ='-'
        token = restartToken(matrix)
    else:
        snake.insert(0,newhead)
        matrix[newhead[0]][newhead[1]] = '@'
        matrix[snake[1][0]][snake[1][1]] = 'x'
        matrix[snake[len(snake)-1][0]][snake[len(snake)-1][1]] ='-'
        snake.pop()
    return snake

def snakeUp(snake,matrix,token):

    newhead = [snake[0][0]-1,snake[0][1]]
    if (newhead == token):
        snake.insert(0,newhead)
        matrix[newhead[0]][newhead[1]] = '@'
        matrix[snake[1][0]][snake[1][1]] = 'x'
        matrix[snake[len(snake)-1][0]][snake[len(snake)-1][1]] ='-'
        token = restartToken(matrix)
    else:
        snake.insert(0,newhead)
        matrix[newhead[0]][newhead[1]] = '@'
        matrix[snake[1][0]][snake[1][1]] = 'x'
        matrix[snake[len(snake)-1][0]][snake[len(snake)-1][1]] ='-'
        snake.pop()
    return snake

def snakeDown(snake,matrix,token):

    newhead = [snake[0][0]+1,snake[0][1]]
    if (newhead == token):
        snake.insert(0,newhead)
        matrix[newhead[0]][newhead[1]] = '@'
        matrix[snake[1][0]][snake[1][1]] = 'x'
        matrix[snake[len(snake)-1][0]][snake[len(snake)-1][1]] ='-'
        token = restartToken(matrix)
    else:
        snake.insert(0,newhead)
        matrix[newhead[0]][newhead[1]] = '@'
        matrix[snake[1][0]][snake[1][1]] = 'x'
        matrix[snake[len(snake)-1][0]][snake[len(snake)-1][1]] ='-'
        snake.pop()
    return snake
    
def snakeDead(matrix,head,snake):
    
    lst = ArrayToList(snake)
    for i in range(0, len(snake), 1):
        if(head == lst[1]):
            return True
        else:
            return False

def placeToken(matrix):

    token = '*'
    matrix[9][14] = token
    return [9,14]

def restartToken(matrix):

    token = "*"
    x = random.randint(0,29)
    y = random.randint(0,19)
    matrix[y][x] = token
    return [y,x]

main()
