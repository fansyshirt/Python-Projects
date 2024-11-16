import random
import math
import pygame

pygame.font.init()
num_font = pygame.font.SysFont("Arial", 60, bold=True)

colour_list = [(255, 255, 255), (238, 228, 218), (237, 224, 200), (242, 177, 121), (245, 149, 99), (246, 124, 95),
               (246, 94, 59), (237, 207, 114), (237, 204, 97), (237, 200, 80), (237, 200, 0), (255, 255, 0)]

grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
run = 1
fps = 60

X, Y = 600, 600
win = pygame.display.set_mode((X, Y))

pygame.display.set_caption("2048 game")

rect_list = []
for axis_y in range(4):
    for axis_x in range(4):
        rec = pygame.Rect(35 + axis_x * 135, 35 + axis_y * 135, 125, 125)
        rect_list.append(rec)
print(rect_list)


def combine(full_list):
    for item in full_list:
        if item[0] == item[1]:
            item[0] = item[0] * 2
            item[1] = 0
        if item[1] == item[2]:
            item[1] = item[1] * 2
            item[2] = 0
        if item[2] == item[3]:
            item[2] = item[2] * 2
            item[3] = 0
    return full_list


def compress(full_list):
    new_list = []
    for lis in full_list:
        i = 0
        empty = []
        full = []
        for item in lis:
            if item == 0:
                empty.append(lis[i])
            else:
                full.append(lis[i])
            i += 1
        new_list.append(full + empty)
    return new_list


def show():
    for item in grid:
        pass
        print(item)
    print()


def random_gen(run):
    i = 0
    empty = []
    for row in grid:
        for item in row:
            if item == 0:
                empty.append(i)
            i += 1
    if len(empty) == 0:
        run = 0
    else:
        val1 = random.randint(0, len(empty)-1)
        chosen = empty[val1]
        val2 = random.randint(0, 10)
        if val2 != 1:
            val3 = 2
        else:
            val3 = 4
        grid[math.floor(chosen//4)][(chosen % 4)] = val3
    return run


def draw_window(grid):
    i = 0
    for lis in grid:
        for item in lis:
            if item != 0:
                pygame.draw.rect(win, colour_list[int(math.log(item, 2))], rect_list[i])
                num_text = num_font.render(str(item), True, (25, 25, 25))
                win.blit(num_text, (rect_list[i].x + rect_list[i].width/2 - num_text.get_width()/2, rect_list[i].y + rect_list[i].height/2 - num_text.get_height()/2))
            else:
                pygame.draw.rect(win, (255, 255, 255), rect_list[i])
            i += 1
    pygame.display.update()


run = random_gen(run)
run = random_gen(run)
show()

clock = pygame.time.Clock()

while True:
    if run == 0:
        grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        run = 1
    clock.tick(fps)
    command = ""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                command = "u"
            if event.key == pygame.K_DOWN:
                command = "d"
            if event.key == pygame.K_LEFT:
                command = "l"
            if event.key == pygame.K_RIGHT:
                command = "r"
    old_grid = grid
    if command == "u":
        list1 = [grid[0][0], grid[1][0], grid[2][0], grid[3][0]]
        list2 = [grid[0][1], grid[1][1], grid[2][1], grid[3][1]]
        list3 = [grid[0][2], grid[1][2], grid[2][2], grid[3][2]]
        list4 = [grid[0][3], grid[1][3], grid[2][3], grid[3][3]]
        full_list = [list1, list2, list3, list4]
        comp_grid = compress(combine(compress(full_list)))
        comp_list1 = [comp_grid[0][0], comp_grid[1][0], comp_grid[2][0], comp_grid[3][0]]
        comp_list2 = [comp_grid[0][1], comp_grid[1][1], comp_grid[2][1], comp_grid[3][1]]
        comp_list3 = [comp_grid[0][2], comp_grid[1][2], comp_grid[2][2], comp_grid[3][2]]
        comp_list4 = [comp_grid[0][3], comp_grid[1][3], comp_grid[2][3], comp_grid[3][3]]
        grid = [comp_list1, comp_list2, comp_list3, comp_list4]
        if grid != old_grid:
            run = random_gen(run)
        show()
    if command == "d":
        list1 = [grid[3][0], grid[2][0], grid[1][0], grid[0][0]]
        list2 = [grid[3][1], grid[2][1], grid[1][1], grid[0][1]]
        list3 = [grid[3][2], grid[2][2], grid[1][2], grid[0][2]]
        list4 = [grid[3][3], grid[2][3], grid[1][3], grid[0][3]]
        full_list = [list1, list2, list3, list4]
        comp_grid = compress(combine(compress(full_list)))
        comp_list1 = [comp_grid[0][3], comp_grid[1][3], comp_grid[2][3], comp_grid[3][3]]
        comp_list2 = [comp_grid[0][2], comp_grid[1][2], comp_grid[2][2], comp_grid[3][2]]
        comp_list3 = [comp_grid[0][1], comp_grid[1][1], comp_grid[2][1], comp_grid[3][1]]
        comp_list4 = [comp_grid[0][0], comp_grid[1][0], comp_grid[2][0], comp_grid[3][0]]
        grid = [comp_list1, comp_list2, comp_list3, comp_list4]
        if grid != old_grid:
            run = random_gen(run)
        show()
    if command == "l":
        grid = compress(combine(compress(grid)))
        if grid != old_grid:
            run = random_gen(run)
        show()
    if command == "r":
        list1 = grid[0][::-1]
        list2 = grid[1][::-1]
        list3 = grid[2][::-1]
        list4 = grid[3][::-1]
        full_list = [list1, list2, list3, list4]
        comp_grid = compress(combine(compress(full_list)))
        comp_list1 = comp_grid[0][::-1]
        comp_list2 = comp_grid[1][::-1]
        comp_list3 = comp_grid[2][::-1]
        comp_list4 = comp_grid[3][::-1]
        grid = [comp_list1, comp_list2, comp_list3, comp_list4]
        if grid != old_grid:
            run = random_gen(run)
        show()
    draw_window(grid)
