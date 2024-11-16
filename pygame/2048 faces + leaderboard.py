import random
import math
import pygame

pygame.font.init()
font1 = pygame.font.SysFont("Arial", 20)
font2 = pygame.font.SysFont("Arial", 25)

keys = {
    8: "delete",
    97: "A",
    98: "B",
    99: "C",
    100: "D",
    101: "E",
    102: "F",
    103: "G",
    104: "H",
    105: "I",
    106: "J",
    107: "K",
    108: "L",
    109: "M",
    110: "N",
    111: "O",
    112: "P",
    113: "Q",
    114: "R",
    115: "S",
    116: "T",
    117: "U",
    118: "V",
    119: "W",
    120: "X",
    121: "Y",
    122: "Z"
}

colour_list = [(255, 255, 255), (238, 228, 218), (237, 224, 200), (242, 177, 121), (245, 149, 99), (246, 124, 95),
               (246, 94, 59), (237, 207, 114), (237, 204, 97), (237, 200, 80), (237, 200, 0), (255, 255, 0)]

grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
run = 1
fps = 60

X, Y = 600, 600
win = pygame.display.set_mode((X, Y))

pygame.display.set_caption("2048 game")

doc = open("./hidden/save.txt", "r")
doc = doc.read()
doc = doc.split("\n")

highscores = []
for item in doc:
    score = item.split(":")
    highscores.append(score)
print(highscores)

i_01 = pygame.image.load("./faces/08.png")
i_01 = pygame.transform.scale(i_01, (125, 125))
i_02 = pygame.image.load("./faces/11.png")
i_02 = pygame.transform.scale(i_02, (125, 125))
i_03 = pygame.image.load("./faces/03.png")
i_03 = pygame.transform.scale(i_03, (125, 125))
i_04 = pygame.image.load("./faces/01.png")
i_04 = pygame.transform.scale(i_04, (125, 125))
i_05 = pygame.image.load("./faces/05.png")
i_05 = pygame.transform.scale(i_05, (125, 125))
i_06 = pygame.image.load("./faces/09.png")
i_06 = pygame.transform.scale(i_06, (125, 125))
i_07 = pygame.image.load("./faces/02.png")
i_07 = pygame.transform.scale(i_07, (125, 125))
i_08 = pygame.image.load("./faces/06.png")
i_08 = pygame.transform.scale(i_08, (125, 125))
i_09 = pygame.image.load("./faces/04.png")
i_09 = pygame.transform.scale(i_09, (125, 125))
i_10 = pygame.image.load("./faces/07.png")
i_10 = pygame.transform.scale(i_10, (125, 125))
i_11 = pygame.image.load("./faces/10.png")
i_11 = pygame.transform.scale(i_11, (125, 125))



rect_list = []
for axis_y in range(4):
    for axis_x in range(4):
        rec = pygame.Rect(35 + axis_x * 135, 35 + axis_y * 135, 125, 125)
        rect_list.append(rec)


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


def draw_window(grid, score, lose, leaderboard, highscore, name):
    box = pygame.Rect(0, 0, 600, 600)
    pygame.draw.rect(win, (0, 0, 0), box)

    i = 0
    for lis in grid:
        for item in lis:
            if item != 0:
                if item == 2:
                    win.blit(i_01, (rect_list[i].x, rect_list[i].y))
                if item == 4:
                    win.blit(i_02, (rect_list[i].x, rect_list[i].y))
                if item == 8:
                    win.blit(i_03, (rect_list[i].x, rect_list[i].y))
                if item == 16:
                    win.blit(i_04, (rect_list[i].x, rect_list[i].y))
                if item == 32:
                    win.blit(i_05, (rect_list[i].x, rect_list[i].y))
                if item == 64:
                    win.blit(i_06, (rect_list[i].x, rect_list[i].y))
                if item == 128:
                    win.blit(i_07, (rect_list[i].x, rect_list[i].y))
                if item == 256:
                    win.blit(i_08, (rect_list[i].x, rect_list[i].y))
                if item == 512:
                    win.blit(i_09, (rect_list[i].x, rect_list[i].y))
                if item == 1024:
                    win.blit(i_10, (rect_list[i].x, rect_list[i].y))
                if item == 2048:
                    win.blit(i_11, (rect_list[i].x, rect_list[i].y))
            else:
                pygame.draw.rect(win, (255, 255, 255), rect_list[i])
            i += 1
    line = pygame.Rect(0, 0, 500, 35)
    pygame.draw.rect(win, (0, 0, 0), line)
    text = font1.render("score: " + str(score), 0, (255, 255, 255))
    win.blit(text, (30, 10))

    if lose:
        box = pygame.Rect(50, 50, 500, 500)
        pygame.draw.rect(win, (240, 240, 240), box)
        text = font2.render("Congrats, you finished with " + str(score) + " points", 1, (0, 0, 0))
        win.blit(text, (60, 60))
        line = pygame.Rect(50, 150, 500, 2)
        pygame.draw.rect(win, (150, 150, 150), line)

        line = pygame.Rect(150, 150, 2, 350)
        pygame.draw.rect(win, (150, 150, 150), line)
        line = pygame.Rect(50, 150, 2, 350)
        pygame.draw.rect(win, (150, 150, 150), line)
        line = pygame.Rect(548, 150, 2, 350)
        pygame.draw.rect(win, (150, 150, 150), line)
        for i in range(8):
            line = pygame.Rect(50, 150+i*50, 500, 2)
            pygame.draw.rect(win, (150, 150, 150), line)
        i = 0
        cursor = 0
        cursor_place = 0
        for row in highscore:
            if i < 7-cursor_place:
                if int(row[1]) >= score:
                    text = font2.render(row[0], 1, (0, 0, 0))
                    win.blit(text, (60, 160+i*50))
                    text = font2.render(row[1], 1, (0, 0, 0))
                    win.blit(text, (160, 160+i*50))
                    cursor = i+1
                else:
                    cursor_place = 1
                    text = font2.render(row[0], 1, (0, 0, 0))
                    win.blit(text, (60, 160 + (i+1) * 50))
                    text = font2.render(row[1], 1, (0, 0, 0))
                    win.blit(text, (160, 160 + (i+1) * 50))
            i+=1

        if leaderboard:
            text = font2.render("Enter your name for the leaderboard", 1, (0, 0, 0))
            win.blit(text, (60, 110))
            text = font2.render(name, 1, (0, 0, 0))
            win.blit(text, (60, 160 + cursor * 50))
            text = font2.render(str(score), 1, (0, 0, 0))
            win.blit(text, (160, 160+cursor*50))
        else:
            text = font2.render("You did not place on the leaderboard", 1, (0, 0, 0))
            win.blit(text, (60, 110))

        button = pygame.Rect(225, 505, 150, 40)
        pygame.draw.rect(win, (200, 200, 200), button)
        line = pygame.Rect(225, 505, 150, 2)
        pygame.draw.rect(win, (150, 150, 150), line)
        line = pygame.Rect(225, 505, 2, 40)
        pygame.draw.rect(win, (150, 150, 150), line)
        line = pygame.Rect(225, 545, 150, 2)
        pygame.draw.rect(win, (150, 150, 150), line)
        line = pygame.Rect(373, 505, 2, 40)
        pygame.draw.rect(win, (150, 150, 150), line)

        text = font2.render("restart", 1, (0, 0, 0))
        win.blit(text, (300 - text.get_width()//2, 510))

    pygame.display.update()


run = random_gen(run)
run = random_gen(run)
#show()

clock = pygame.time.Clock()

player = ""
lose = 0
leaderboard = 0
mouse_pos = (0, 0)

while True:
    if run == 0:
        grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        run = 1
    clock.tick(fps)
    command = ""
    clicked = 0
    pressed = 0
    key_press = ""
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
            try:
                key_press = keys[event.key]
                pressed = 1
            except:
                # print("error")
                pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = 1

    mouse_presses = pygame.mouse.get_pressed()
    if mouse_presses[0]:
        mouse_pos = pygame.mouse.get_pos()
    if 225 < mouse_pos[0] < 375 and 505 < mouse_pos[1] < 545 and len(player) > 1 and lose == 1 and clicked: #225, 505, 150, 40
        grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        run = random_gen(run)
        run = random_gen(run)
        if leaderboard:
            new_leaderboard = []
            add = 0
            for row in highscores:
                if int(row[1]) >= score:
                    new_leaderboard.append(row)
                elif int(row[1]) < score and add == 0:
                    new_leaderboard.append([player, str(score)])
                    new_leaderboard.append(row)
                    add = 1
                else:
                    new_leaderboard.append(row)
            print(new_leaderboard)
            f = open("./hidden/save.txt", "w")
            text = ""
            for row in new_leaderboard:
                text += str(row[0])+":"+str(row[1])+"\n"
            text = text[:-1]
            f.write(text)
            f.close()
            highscores = new_leaderboard
        player = ""
        lose = 0
        leaderboard = 0
        mouse_pos = (0, 0)
        #restart

    old_grid = grid

    lose_check_count = 0
    score = 0
    for row in grid:
        for item in row:
            if item != 0:
                lose_check_count += 1
            score += item

    if lose_check_count == 16:
        lose_check = 1
        if grid[0][0] == grid[0][1] or grid[0][1] == grid[0][2] or grid[0][2] == grid[0][3] or grid[1][0] == grid[1][1]\
                or grid[1][1] == grid[1][2] or grid[1][2] == grid[1][3] or grid[2][0] == grid[2][1] or \
                grid[2][1] == grid[2][2] or grid[2][2] == grid[2][3] or grid[3][0] == grid[3][1] or \
                grid[3][1] == grid[3][2] or grid[3][2] == grid[3][3] or grid[0][0] == grid[1][0] or \
                grid[1][0] == grid[2][0] or grid[2][0] == grid[3][0] or grid[0][1] == grid[1][1] or \
                grid[1][1] == grid[2][1] or grid[2][1] == grid[3][1] or grid[0][2] == grid[1][2] or \
                grid[1][2] == grid[2][2] or grid[2][2] == grid[3][2] or grid[0][3] == grid[1][3] or \
                grid[1][3] == grid[2][3] or grid[2][3] == grid[3][3]:
            lose_check = 0
        if lose_check == 1:
            lose = 1
            i = 0
            for item in highscores:
                if i < 7:
                    if score > int(item[1]):
                        leaderboard = 1
                i+=1
    if lose and pressed:
        if key_press != "delete" and len(player) < 4:
            player = player + key_press
        if key_press == "delete":
            player = player[:-1]


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
        #show()
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
        #show()
    if command == "l":
        grid = compress(combine(compress(grid)))
        if grid != old_grid:
            run = random_gen(run)
        #show()
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
        #show()
    draw_window(grid, score, lose, leaderboard, highscores, player)
