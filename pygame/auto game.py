import pygame
import random

X, Y = 500, 500
win = pygame.display.set_mode((X, Y))
fps = 60

pygame.display.set_caption("auto game")

max_y = 10
max_x = 10

grid = []
for item in range(0, max_x):
    string = '[["", 4, 4, 4, 4]' + ', ["", 4, 4, 4, 4]'*(max_x-1) + ']'
for item in range(0, max_y):
    exec_string = 'grid = [' + string + (', '+string)*(max_y-1) + ']'
print(exec_string)
exec(exec_string)

i = 0
for row in grid:
    if i == 0 or i == max_y-1:
        for item in range(0, len(row)):
            row[item] = "x"
    row[0] = "x"
    row[max_x-1] = "x"
    i += 1

player_start = 1, 1
player_x, player_y = player_start

ai_frame = 1

grid[1][1][0] = "P"
grid[max_y-2][max_x-2][0] = "F"


def ai_move(grid, player_x, player_y):
    move_call = 0
    total = grid[player_y][player_x][1] + grid[player_y][player_x][2] + grid[player_y][player_x][3] + grid[player_y][player_x][4]
    rand1 = random.randint(1, total)
    if rand1 <= grid[player_y][player_x][1]:
        move_call = 1
    elif rand1 <= grid[player_y][player_x][1] + grid[player_y][player_x][2]:
        move_call = 2
    elif rand1 <= grid[player_y][player_x][1] + grid[player_y][player_x][2] + grid[player_y][player_x][3]:
        move_call = 3
    else:
        move_call = 4
    return move_call


def move(grid, move_call, player_x, player_y, moves):
    success = 1
    if move_call == 1:
        if grid[player_y-1][player_x][0] != "x" and grid[player_y-1][player_x][0] != "X" and grid[player_y-1][player_x][0] != "a" and [player_x, player_y-1] not in moves:
            grid[player_y][player_x][0] = ""
            grid[player_y-1][player_x][0] = "P"
            player_y -= 1
            moves.append([player_x, player_y])
        elif grid[player_y][player_x - 1][0] == "F":
            success = 2
        elif [player_x, player_y-1] in moves:
            success = 3
        else:
            success = 0
    if move_call == 2:
        if grid[player_y][player_x+1][0] != "x" and grid[player_y][player_x+1][0] != "X" and grid[player_y][player_x+1][0] != "a" and [player_x+1, player_y] not in moves:
            grid[player_y][player_x][0] = ""
            grid[player_y][player_x+1][0] = "P"
            player_x += 1
            moves.append([player_x, player_y])
        elif grid[player_y][player_x - 1][0] == "F":
            success = 2
        elif [player_x+1, player_y] in moves:
            success = 3
        else:
            success = 0
    if move_call == 3:
        if grid[player_y+1][player_x][0] != "x" and grid[player_y+1][player_x][0] != "X" and grid[player_y+1][player_x][0] != "a" and [player_x, player_y+1] not in moves:
            grid[player_y][player_x][0] = ""
            grid[player_y+1][player_x][0] = "P"
            player_y += 1
            moves.append([player_x, player_y])
        elif grid[player_y][player_x - 1][0] == "F":
            success = 2
        elif [player_x, player_y+1] in moves:
            success = 3
        else:
            success = 0
    if move_call == 4:
        if grid[player_y][player_x-1][0] != "x" and grid[player_y][player_x-1][0] != "X" and grid[player_y][player_x-1][0] != "a" and [player_x-1, player_y] not in moves:
            grid[player_y][player_x][0] = ""
            grid[player_y][player_x-1][0] = "P"
            player_x -= 1
            moves.append([player_x, player_y])
        elif grid[player_y][player_x - 1][0] == "F":
            success = 2
        elif [player_x-1, player_y] in moves:
            success = 3
        else:
            success = 0
    return grid, success, player_x, player_y, moves


def draw_win(grid):
    bg = pygame.Rect(0, 0, X, Y)
    pygame.draw.rect(win, (90, 90, 90), bg)
    y = 0
    for row in grid:
        x = 0
        for item in row:
            if item[0] == "x":
                colour = (70, 200, 70)
            elif item[0] == "X":
                colour = (150, 210, 150)
            elif item[0] == "F":
                colour = (0, 0, 0)
            elif item[0] == "a":
                colour = (200, 120, 120)
            else:
                colour = (200, 200, 200)
            square = pygame.Rect(10+((X-20)//max_x)*x, 10+((Y-20)//max_y)*y, ((X-20)//max_x)-5,((Y-20)//max_y)-5)
            pygame.draw.rect(win, colour, square)
            if item[0] == "P":
                colour = (200, 120, 120)
                square = pygame.Rect(10+((X-20)//max_x)*x + (X-20)//(max_x*2) - (X-20)//(max_x*4), 10+((Y-20)//max_y)*y + (Y-20)//(max_y*2) - (Y-20)//(max_x*4), (((X - 20) // max_x) - 5)//2, (((Y - 20) // max_y) - 5)//2)
                pygame.draw.rect(win, colour, square)
            x += 1
        y += 1

    pygame.display.update()


def main(grid, player_x, player_y, ai_frame):
    clock = pygame.time.Clock()
    run = 1
    mouse_x = 0
    mouse_y = 0
    frame = 0
    ai_move_allow = 0
    moves = [[player_x, player_y]]
    success = 1
    while run:
        click = 0
        frame += 1
        frame %= ai_frame
        move_call = 0
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_call = 1
                if event.key == pygame.K_DOWN:
                    move_call = 3
                if event.key == pygame.K_LEFT:
                    move_call = 4
                if event.key == pygame.K_RIGHT:
                    move_call = 2
                if event.key == pygame.K_SPACE:
                    ai_move_allow += 1
                    ai_move_allow %= 2
                    print(ai_move_allow)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = 1
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0] and click == 1:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = (mouse_pos[0] - 10)//((X-20)//max_x)
            mouse_y = (mouse_pos[1] - 10)//((Y-20)//max_y)
            if grid[mouse_y][mouse_x][0] != "x" and grid[mouse_y][mouse_x][0] != "P" and grid[mouse_y][mouse_x][0] != "F":
                if grid[mouse_y][mouse_x][0] == "X":
                    grid[mouse_y][mouse_x][0] = ""
                else:
                    grid[mouse_y][mouse_x][0] = "X"
        if frame == 0 and ai_move_allow == 1:
            move_call = ai_move(grid, player_x, player_y)
        grid, success, player_x, player_y, moves = move(grid, move_call, player_x, player_y, moves)
        if success == 0:
            grid[player_y][player_x][move_call] -= 1
            grid[player_y][player_x][0] = ""
            player_x, player_y = player_start
            grid[player_y][player_x][0] = "P"
            moves = [[player_x, player_y]]
        if success == 2:
            pass
        if success == 3:
            grid[player_y][player_x][move_call] -= 1
            grid[player_y][player_x][0] = ""
            player_x, player_y = player_start
            grid[player_y][player_x][0] = "P"
            moves = [[player_x, player_y]]
        y = 0
        for row in grid:
            x = 0
            for item in row:
                if item[0] != "x":
                    if item[1] + item[2] + item[3] + item[4] == 0:
                        item[0] = "a"
                x += 1
            y += 1
        draw_win(grid)


if __name__ == "__main__":
    main(grid, player_x, player_y, ai_frame)