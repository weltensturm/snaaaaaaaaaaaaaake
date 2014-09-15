
from random import randint
import sys, time, msvcrt, os

timeout = 1/4
def sleep_input():
    startTime = time.time()
    inp = None
    while True:
        if not inp and msvcrt.kbhit():
            inp = msvcrt.getch()
        elif time.time() - startTime > timeout:
            break
    return inp


board = [50, 25]

snake = [(0, 0)]

food = [
    (5, 1),
    ]

def move(x, y):
    global snake
    global food
    global timeout
    new_x = snake[0][0]+x
    new_y = snake[0][1]+y
    if new_x >= board[0]:
        new_x = 0
    if new_x < 0:
        new_x = board[0]-1
    if new_y >= board[1]:
        new_y = 0
    if new_y < 0:
        new_y = board[1]-1
    snake.insert(0, (new_x, new_y))
    tail = snake[-1]
    snake = snake[:-1]
    for i in range(len(food)):
        if food[i][0] == snake[0][0] and food[i][1] == snake[0][1]:
            snake.append(tail)
            timeout *= 0.9
            food = food[:i]
            food.append((randint(0, board[0]-1), randint(0, board[1]-1)))
            break
    for i in range(1, len(snake)):
        if snake[i] == snake[0]:
            snake = snake[:i]
            break

dir=(1,0)

def game():
    global dir
    while True:
        direction = sleep_input()
        if direction == b'w':
            dir = (0, -1)
        elif direction == b's':
            dir = (0, 1)
        elif direction == b'a':
            dir = (-1, 0)
        elif direction == b'd':
            dir = (1, 0)
        elif direction == b'q':
            return
        move(*dir)
        os.system('cls')
        for y in range(board[1]):
            for x in range(board[0]):
                found = False
                for segment in snake:
                    if segment[0] == x and segment[1] == y:
                        sys.stdout.write('*')
                        found = True
                        break
                if not found:
                    for ent in food:
                        if ent[0] == x and ent[1] == y:
                            sys.stdout.write('+')
                            found = True
                            break
                if not found:
                    sys.stdout.write(' ')
            print()


game()

